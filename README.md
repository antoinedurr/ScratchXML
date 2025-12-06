# ScratchXML
Python module to read and write Assimilate Scratch custom-command XML output.

### Description
The _ScratchXML_ module converts an XML hierarchy output by [Assimilate Scratch](https://www.assimilateinc.com/products/) into an object based hierarchy.
It defines Scratch(), Construct(), Slot(), and Shot() classes that closely mirror the XML.

The typical use case is in support of a Scratch [Custom Command](https://www.assimilatesupport.com/akb/KnowledgebaseArticle51000.aspx).
Invoking the custom command exports XML, runs your script, then ingests the output. 
Within your script, the XML is read when the Scratch() object is created.  You now manipulate the hierarchy, then write out the result.

The scratchXML module refactors the XML output into the corresponding hierarchy of ScratchElement instances.
The resulting data can be easily examined using in a dictionary or attribute approach, e.g. `shot['length']` or `shot.length`.
Elements that are inline, e.g. the `uuid` in <shot uuid='123456789123456789'> are imported and accessible as `shot['@uuid']` or `shot.uuid`.
You can also create Scratch timelines from -- scratch, then output the XML and read them into Scratch.

### Dependencies
This module depends on the [xml2dict](https://pypi.org/project/XML2Dict/) module.

### Installing
```
pip install git+https://github.com/antoinedurr/ScratchXML
```

### Using/Importing
The most typical approach is to process XML output by Scratch.  To do this you'll need to:
```
from scratchXML import Scratch
```

If you are creating an XML file from the ground up, then you'll need to import the rest:
```
from scratchXML import Scratch, Construct, Slot, Shot
```

The module also defines some utilities that make custom commands easier to write:
```
from scratchXML import scratchparse, shotinfo
```

### Examples
#### Print shots and metadata
```
from scratchXML import Scratch
scratch = Scratch(xml='cmd-0.xml')  # read cmd-0.xml and convert into a Scratch() hierarchy

for construct in scratch.constructs: # iterate through all the constructs (there will be only one)
  for slot in construct.slots: # iterate through all the slots
    for shot in slot.shots: # finally, iterate through all the shots
      print(f"Shot: {shot.name} ({shot.slot} {shot.layer} Metadata: {shot.metadata}") # print out metadata for each shot
```
Attributes on objects can be read as attributes or dictionary elements (shot['name'] == shot.name).  However, they currently can only be updated as dictionary elements.

#### Print shots and metadata (easier)
There are some convenience methods, e.g. a Construct() has a shots() method, so the above could be shortened to:
```
from scratchXML import Scratch
scratch = Scratch(xml='cmd-0.xml')  # read cmd-0.xml and convert into a Scratch() hierarchy
shots = scratch.construct[0].shots()

for shot in shots: # finally, iterate through all the shots
  print(f"Shot: {shot.name} ({shot.slot} {shot.layer} Metadata: {shot.metadata}") # print out metadata for each shot
```

#### Reverse shot order within slots
A more sophisticated usage reverses shot versions within a slot:
```
from scratchXML import Scratch
scratch = Scratch(xml='cmd-0.xml')  # read cmd-0.xml and convert into a Scratch() hierarchy

for construct in scratch.constructs:
  for slot in s.constructs[0].slots:
    slot.shots = reversed(slot.shots)  # see limitations
s['update'] = "Y" # tell Scratch to update from the resulting xml
s.write('res-0.xml')  # write out resulting file
```

#### Create XML from scratch
You can also create a Scratch timeline from the ground up, though this approach is not yet well supported:
```
from scratchXML import Scratch
scratch = Scratch()  # start with a blank slate

s = Scratch()
s.constructs.append(Slot())
s.constructs[0].slots[0].append(Shot())
s.write(xml="new.xml")
```

### Limitations
- As of November 2025, only Timeline exports are handled.  These can be with or without selected shots.
- Scratch XML doesn't contain the _entire_ project.  For example, only base grades are included, layers are not
- when reading XML back in, Scratch won't rearrange shots -- it's really only designed to modify shots in place
  - the solution to the above is to manually import the output XML into Scratch.
