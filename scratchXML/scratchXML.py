#!/usr/local/bin/python3
#
# A library for Assimilate Scratch 
#
import xmltodict
import pprint
import re

class Lineage:
    '''
    Simple container to name our 3 items and make sure that _lineage is properly defined
    '''
    def __init__(self, collective: str, child: str, childclass: type['ScratchElement']):
        self.collective = collective # e.g. 'constructs'
        self.child = child # e.g. 'construct'
        self.childclass = childclass # e.g. Construct


class ScratchElementList(list):
    '''
    ScratchElementList is a list subclass that only allows ScratchElement instances to be added.
    i.e. you can only add a Slot to the Slots list, etc.  Ultimatelly, this will support a new() method
    which will automatically add the correct element type.
    '''
    def __init__(self, initial_elements=None):
        if not isinstance(ScratchElement, type):
            raise TypeError("allowed_type must be a type.")

        if initial_elements is not None:
            if not all(isinstance(elem, ScratchElement) for elem in initial_elements):
                raise TypeError("All initial elements must be of type ScratchElement.")
            super().__init__(initial_elements)
        else:
            super().__init__()

    def _validate_item(self, item):
        if not isinstance(item, ScratchElement):
            raise TypeError("Only objects of type ScratchElement can be added to this list.")

    def append(self, item):
        self._validate_item(item)
        super().append(item)

    def insert(self, index, item):
        self._validate_item(item)
        super().insert(index, item)

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            if not all(isinstance(elem, self._allowed_type) for elem in value):
                raise TypeError(
                    f"All elements in the slice assignment must be of type {self._allowed_type.__name__}.")
        else:
            self._validate_item(value)
        super().__setitem__(key, value)

    def extend(self, iterable):
        if not all(isinstance(item, self._allowed_type) for item in iterable):
            raise TypeError("All elements in the iterable must be of type ScratchElement.")
        super().extend(iterable)



class ScratchElement:
    """
    The superclass for Scratch.  Provides a dictionary and attribute lookups of the XML dictionary.
    Most importantly, it defines parsechildren() and unparsechildren(), which takes a dict structure like
    constructs{construct: [list of constructs]} and replaces them with a list of [construct()] instances
    """
    def __init__(self, xmldict=None, lineage=None, parsemeta=False):
        self._lineage = lineage # we'll need this for the unparsing
        self.xmldict = {} # this contains our dictionary from the XML export from Scratch

        if xmldict:
            self.xmldict = xmldict
            if lineage: # will be None if we're at bottom of hierarchy, i.e. shots don't have children
                self.parsechildren(lineage)
            if parsemeta: # only applies to shots, afaik
                self.parsemeta()


    # present the self.xmldict as a dictionary
    def __getitem__(self, key):
        return self.xmldict.__getitem__(key)

    def __setitem__(self, key, value):
        self.xmldict.__setitem__(key, value)

    def get(self, key, default=None):
        return self.xmldict.get(key, default)
    
    def keys(self):
        return self.xmldict.keys()
    
    # present the self.xmldict as attributes
    def __getattr__(self, key):
        if key in self.xmldict:
            return self.xmldict[key]
        elif '@'+key in self.xmldict:
            return self.xmldict['@'+key]
        else:
            raise AttributeError(f"{self.__class__.__name__} object has no attribute '{key}'")
    
    def __setattr__(self, key, val):
        super().__setattr__(key, val)

    def __repr__(self):
        type_ = type(self)
        module = type_.__module__
        qualname = type_.__qualname__
        if '@name' in self.xmldict or 'name' in self.xmldict:
            name = self.name  # will resolve even w/out the @
        elif '@project' in self.xmldict:
            name = self.project  # for top level Scratch object
        else:
            if '@index' in self.xmldict:
                # for slots since they only have indices
                name = f"{qualname} {self.index}"
            else:
                name = f"{qualname}"

        # return f'<{module}.{qualname} object "{name}" at {hex(id(self))}>'
        return f'<{module}.{qualname} object "{name}" at {hex(id(self))}>'

        # return f"<{self.__class__.__name__} <{self.name}> {hex(id(self))}>"

    def parsechildren(self, lineage: Lineage):

        '''
        This method converts a collective dict to an array of element instances.  It returns
        a dict that can be used to update the xmldict of the object.

        For example, in the XML you have <slots> <slot>...</slot> <slot>...</slot> </slots>.  This 
        get converted to the dictionary {slots: [{slot: {...}}]}.
        parsechildren() will convert that to {'slots': [Slot(...), Slot(...)]}.

        It is called at the top from Scratch during the XML read phase, converts its children,
        and asks each in turn to convert their children.

        This is done through the constructors, when they are fed xmldict's, they go and parse 
        '''
        # print(f"self: {self}, {lineage.collective} {self.xmldict.keys()}")

        # deal with things like empty slots
        if lineage.collective not in self.xmldict or self.xmldict.get(lineage.collective) is None: # if 'slots' not in self.xmldict
            self.xmldict[lineage.collective] = {}

        collection = [lineage.childclass(xmldict=elem) for elem in self.xmldict.get(lineage.collective, {}).get(lineage.child, [])]

        # the ScratchElementList ensures that only the correct type of element can be added
        self.xmldict[lineage.collective] = ScratchElementList(collection) # make it a list, e.g. [Slot(), Slot(), ...]


    def unparsechildren(self):
        '''
        This is called recursively to undo the objectification of the element array
        '''
        if self._lineage:
            temp = {self._lineage.child: [element.unparsechildren() for element in self.xmldict[self._lineage.collective]]} # expand constructs
            return {**self.xmldict, **{self._lineage.collective: temp}}  # and superimpose it 
        else:
            return {**self.xmldict} # bottom of the hierarchy

    def parsemeta(self):
        '''
        Refactor the dict of dataitems into a simple key:value dictionary of metadata name, metadata value
        '''
        if 'metadata' not in self.xmldict:
            self.xmldict['metadata'] = {}

        self.xmldict['metadata'] = {d['key']: d['value']
                                    for d in self.xmldict['metadata'].get('dataitem', [])}

    def unparsemeta(self):
        '''
        Undo the metadata dict back to a dataitem array
        '''
        if 'metadata' in self.xmldict:
            self.xmldict['metadata'] = {'dataitem': [{'key': k, 'value': v} for k, v in self.xmldict['metadata'].items()]}


class Scratch(ScratchElement):
    """
    The root class for Scratch, the only one that needs to be explicitly imported.  This class
    has the XML reader and writer, and then everything expands from there.
    """
    def __init__(self, xml=None):
        self._lineage = Lineage('constructs', 'construct', Construct)
        # super().__init__(None, self._lineage, parsemeta=True)
        xmldict = {}

        if xml:
            xmldict = self.read(xml=xml)['scratch'] # bootstrap into hierarchy
        
        super().__init__(xmldict, self._lineage, parsemeta=True) # rerun the ScratchElement constructor which will invoke parsechildren

    def read(self, xml=None):
        '''
        Read an XML file and return the parsed dictionary.
        
        :param xml: Filepath of XML file.
        '''
        if xml:
            with open(xml, 'r') as fp:
                file_content = fp.read()

                # this is the raw xml.  When user wants a group, for example, we need to see if dict is properly parsed
                return xmltodict.parse(file_content, force_list=["construct", "slot", "shot", "dataitem"]) # force these items to always be lists
        return None

    def write(self, xml=None):
        '''
        Write the current dictionary to an XML file.
        
        :param xml: Filepath of XML file.
        '''
        if xml:
            self.xmldict = self.unparsechildren()

            # print("unparsedchildren after:")
            # pprint.pprint(self.xmldict)
            with open(xml, 'w') as fp:
                file_content = xmltodict.unparse({'scratch': self.xmldict}, pretty=True) # unbootstrapped dict has single key, 'scratch'
                fp.write(file_content) 

# ---------------------------------------------------------------------

class Group(ScratchElement):
    pass

# ---------------------------------------------------------------------

class Construct(ScratchElement):
    '''
    Object representation of a Scratch Construct, which contains Slots
    '''
    def __init__(self, xmldict=None):
        self._lineage = Lineage('slots', 'slot', Slot)
        super().__init__(xmldict, self._lineage)

    def shots(self, selected=None, bottom_row=None, uuid_only=False):
        '''
        Return the shots in this timeline construct

        selected: if True, return only the selected shots
        bottom_row: if True, return only the shots in the bottom row (slot 0)
        uuid_only: if True, return only the UUIDs of the selected shots
        '''

        shots = []
        for slot in self.slots:
            for shot in slot.shots:
                include_sel = True
                include_bot = True
                if selected is True and shot.get('@selected') != "Y":
                    include_sel = False
                if selected is False and shot.get('@selected') == "Y":
                    include_sel = False
                if bottom_row is True and shot.layer != 0:
                    include_bot = False
                if bottom_row is False and shot.layer == 0:
                    include_bot = False

                if include_sel and include_bot:
                    shots.append(shot)

        if uuid_only:
            shots = [shot.uuid for shot in shots]

        return shots

    def slotnames(self, regex):
        '''
        Return the names of the slots in this construct, optionally filtered by a regex.

        :param regex: Regular expression to filter slot names.
        '''
        slot_names = {}

        for slot in self.slots:
            if slot.shots:
                shot = slot.shots[0]

                match = re.match(regex, shot.name)
                if match:
                    shotname = match.group(0)
                    if shotname not in slot_names: # don't accept duplicates
                        slot_names[shotname] = slot.index

        return slot_names
    
class Slot(ScratchElement):
    '''
    Object representation of a Scratch Slot, which contains Shots
    '''
    def __init__(self, xmldict=None):
        self._lineage = Lineage('shots', 'shot', Shot)
        super().__init__(xmldict, self._lineage)

    @property
    def index(self):
        return int(self.xmldict['@index'])

    # remove the named element
    def removeshot(self, removeshot):
        '''
        Remove shot from the slot.  Expects a Shot instance, from which it will match the UUID.
        
        :param removeshot: Shot() instance to remove
        '''
        # print(f"removeshot(): Removing shot {removeshot['@uuid']} from slot {self.index}")
        self.xmldict['shots'] = [shot for shot in self.xmldict['shots'] if shot['@uuid'] != removeshot['@uuid']]
        self.renumbershots()

    def insertshot(self, index, shot):
        '''
        Insert a shot at a specific index in the slot.

        :param index: Position to insert the shot.
        :param shot: Shot instance to insert.
        '''
        self.xmldict['shots'].insert(index, shot) # this time we can use list.insert as
        self.renumbershots()

    # redo the @layer numbering
    def renumbershots(self):
        '''
        Renumber the @layer attributes of all shots in the slot.  This is called automatically after an insertshot 
        or removeshot operation, so that the @layer attributes remain consistent.
        '''
        for index, shot in enumerate(self.xmldict['shots']):
            shot['@layer'] = str(index)
            shot['@slot'] = str(self.xmldict['@index'])

    def listshots(self, prefix=""):
        '''
        List the shots in this slot.

        :param prefix: Often sets of spaces for indentation.
        '''
        for index, shot in enumerate(self.xmldict['shots']):
            print(f"{prefix}Layernum: {index}:", shot.name)

# ---------------------------------------------------------------------

class Shot(ScratchElement):
    '''
    Object representation of a Scratch Shot.  This is also known as a version in the Scratch UI.
    '''
    def __init__(self, xmldict=None):
        self._lineage = None
        super().__init__(xmldict, self._lineage, parsemeta=True)
        
    # def parsechildren(self, lineage: Lineage):
    #     super().parsechildren(lineage)
        # need to figure out how to get this into parsechildren, which currently returns a list
        # self.xmldict['metadata'] = {d['key']: d['value'] for d in self.xmldict['metadata'].get('dataitem', [])}
        
    @property
    def layer(self):
        return int(self.xmldict['@layer'])
    
    @property
    def slot(self):
        return int(self.xmldict['@slot'])
    
    def move(self, sourceslot: Slot, destslot: Slot, destlayer: int):
        '''
        Move this shot from one slot to another at the specified layer.

        :param sourceslot: Source slot
        :type sourceslot: Slot
        :param destslot: Destination slot
        :type destslot: Slot
        :param destlayer: The index in the destination slot where the shot should be inserted
        :type destlayer: int
        '''
        # print(f"move(): Moving shot {self.xmldict['@uuid']} from slot {sourceslot.index} to slot {destslot.index}")
        # shot = sourceslot.shots[self.layer] # get our claws on the shot being relocated
        sourceslot.removeshot(self) # remove from original
        destslot.insertshot(destlayer, self) # and put where it needs to go

    def shotname(self, regex=None):
        '''
        Convenience method to get the name of the shot, or filtered by a regex.
        '''


        if regex is None:
            return self.name
        else:
            match = re.match(regex, self.name)
            if match:
                return match.group(0)
            else:
                return None

