# ScratchXML
Python module to read and write Assimilate Scratch custom-command XML files.

### Description
The _scratchXML_ module converts an XML hierarchy output by [Assimilate Scratch](https://www.assimilateinc.com/products/) into an object based hierarchy.
It defines Scratch(), Construct(), Slot(), and Shot() classes that closely mirror the XML.

The typical use case is in support of a Scratch [Custom Command](https://www.assimilatesupport.com/akb/KnowledgebaseArticle51000.aspx).
Invoking the custom command causes Scratch to export XML, run your script, and then ingest the output. 
Within your script, the XML is read when the Scratch() object is created.  You now manipulate the hierarchy, then write out the result.

The scratchXML module refactors the XML output into the corresponding hierarchy of ScratchElement instances.
The resulting data can be easily examined using in a dictionary or attribute approach, e.g. `shot['length']` or `shot.length`.
Elements that are inline, e.g. the `uuid` in <shot uuid='123456789123456789'> are imported and accessible as `shot['@uuid']` or `shot.uuid`.
You can also create Scratch timelines from -- scratch, then output the XML and read them into Scratch.


### Installing
```
pip install git+https://github.com/antoinedurr/ScratchXML
```
#### Dependencies
This module depends on the [xmltodict](https://pypi.org/project/xmltodict) module which you can get via:
```
pip install xmltodict
```



### Working Examples
The [examples_working folder](https://github.com/antoinedurr/ScratchXML/tree/main/examples_working) contains some fully working Scratch custom commands.

- **scratch_export_csv.py** -- writes out shot info and (optionally) metadata to a .csv file and opens file
- **scratch_playlist2copypaste.py** -- grabs the bottom row of shots and puts the filepaths into the copy/paste buffer

See the Assimilate Scratch Docs for [how to install](https://www.assimilatesupport.com/akb/KnowledgebaseArticle51000.aspx) the custom command into Scratch.

### Getting Started Examples
Each example here is available in the [examples_getting_started folder](https://github.com/antoinedurr/ScratchXML/tree/main/examples_getting_started).
#### Importing Scratch elements

```
# The most typical approach is to process XML output by Scratch.
from scratchXML import Scratch 

# If you are creating an XML file from the ground up, then you'll need to import all the elements
from scratchXML import Scratch, Construct, Slot, Shot

# The module also defines some utilities that make custom commands easier to write:
from scratchXML import scratchparse, shotinfo
```

#### Print shots and metadata
```
from scratchXML import Scratch

# read example1.xml and convert into a Scratch() hierarchy
scratch = Scratch(xml='xml/example1.xml')

# iterate through all the constructs (there will be only one) and print out shot info
for construct in scratch.constructs:
  for slot in construct.slots:  # iterate through all the slots
    for shot in slot.shots:  # finally, iterate through all the shots
      print(f"Shot: {shot.name} slot: {shot.slot} layer: {shot.layer} file: {shot.file}")
```
Attributes on objects can be read as attributes or dictionary elements (shot['name'] == shot.name).  However, they currently can only be updated as dictionary elements.

#### Print shot names and metadata (easier)
There are some convenience methods, e.g. Construct() has a shots() method, so the above could be shortened to:
```
from scratchXML import Scratch
scratch = Scratch(xml='cmd-0.xml')  # read cmd-0.xml and convert into a Scratch() hierarchy
timeline = scratch.constructs[0]
shots = timeline.shots(selected=True) or timeline.shots() # get list of selected shots in timeline, or if no selection, all shots

for shot in shots: # iterate through all the shots
  print(f"Shot: {shot.name} ({shot.slot} {shot.layer}) Metadata: {shot.metadata}") # print out metadata for each shot
```

#### Reverse shot order within slots
A more sophisticated usage reverses shot versions within a slot:
```
from scratchXML import Scratch
scratch = Scratch(xml='cmd-0.xml')  # read cmd-0.xml and convert into a Scratch() hierarchy

for construct in scratch.constructs:
  for slot in s.constructs[0].slots:
    slot.shots = reversed(slot.shots)  # see limitations
scratch['update'] = "Y" # tell Scratch to update from the resulting xml
scratch.write('res-0.xml')  # write out resulting file
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
N.B. this aspect of the code is not well developed as of Nov. 2025, i.e. no default attributes are created as you would expect with an empty slot, blank shot, etc.

#### Parsing the command line
With `scratchparse` you can easily parse the command line to easily create a working Scratch custom-command:
```
from scratchXML import scratchparse

parser = scratchparse(usage="Print out info for each shot, including metadata dict")
args = parser.parse_args()

scratch = Scratch(xml=args.inputxml) # ‘inputxml’ is the standard args attribute for the XML that Scratch writes out to Temp
timeline = scratch.constructs[0]

shots = timeline.shots(selected=True) or timeline.shots()
for shot in shots:
   print(f"Shot: {shot.name} ({shot.slot} {shot.layer}) Metadata: {shot.metadata}") # print out metadata for each shot
```
This reports the following usage message:
```
%> ./scratch_example.py -h
usage: scratch_example.py [-h] <input XML> <output XML>

Print out shot info

positional arguments:
  <input XML>
  <output XML>

options:
  -h, --help    show this help message and exit

Scratch custom command settings:
    Type: Application
    Wait till Finished: On
    XML Export: Timeline
    Require Shot Selection: Off
```

### Limitations
- As of November 2025, only Timeline exports are handled.  These can be with or without selected shots.
- Most attributes need to be modified using dictionary updates, e.g. shot['MOS'] = "N", not shot.MOS = "N".
- Scratch XML doesn't contain the _entire_ project.  For example, only base grades are included, layers are not
- when reading XML back in, Scratch won't rearrange shots -- it's really only designed to modify shots in place
  - the solution to the above is to manually import the output XML into Scratch.
