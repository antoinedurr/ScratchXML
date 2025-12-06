# ScratchXML
Python module to read and write Assimilate Scratch custom-command XML output.

### Description
The _ScratchXML_ module converts an XML hierarchy output by [Assimilate Scratch](https://www.assimilateinc.com/products/) into an object based hierarchy.
It defines Scratch(), Construct(), Slot(), and Shot() classes that closely mirror the XML output from Scratch.
The typical usage is to create a Scratch [Custom Command](https://www.assimilatesupport.com/akb/KnowledgebaseArticle51000.aspx) that reads the XML exported by Scratch prior to running the custom command.
ScratchXML refactors the XML output into the corresponding hierarchy of ScratchElement instances.
The resulting data can be easily examined using in a dictionary or attribute approach, e.g. `shot['length']` or `shot.length`.
Elements that are inline, e.g. the `uuid` in <shot uuid='123456789123456789'> are imported and accessible as `shot['@uuid']` or `shot.uuid`.
You can also create Scratch timelines from -- scratch, then output the XML and read them into Scratch.

### Dependencies
This module depends on the [xml2dict](https://pypi.org/project/XML2Dict/) module.

### Examples
```
s = Scratch(xml='cmd-0.xml')  # this creates a Scratch object
for slot in s.constructs[0].slots:
  for shot in slot.shots:
    print(f"Shot: {shot.name} Metadata: {shot.metadata}") # print out metadata for each shot
```
In the above, `constructs` is a list of `Construct()` objects, `slots` is a list of `Slot()` objects,
and `shots` is the list of `Shot()` in each slot.

A more sophisticated usage reverses shot versions within a slot:
```
s = Scratch(xml='cmd-0.xml')
slotnames = 
for slot in s.constructs[0].slots:
  slot.shots = reversed(slot.shots)  # see limitations
s['update'] = "Y" # tell Scratch to update from the resulting xml
s.write('res-0.xml')  # write out resulting file
```

You can also create a Scratch timeline:
```
s = Scratch()
s.constructs.append(Slot())
s.constructs[0].slots[0].append(Shot())
s.write(xml="new.xml")
```

### Limitations
- As of 2025/11/26 only Timeline exports are handled.  These can be with or without selected shots.
- Scratch XML doesn't contain the _entire_ project.  For example, only base grades are included, layers are not
- when reading XML back in, Scratch won't rearrange shots -- it's really only designed to modify shots in place
- the solution to the above is to manually import the XML that the custom command wrote out.
