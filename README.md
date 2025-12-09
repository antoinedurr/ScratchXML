# ScratchXML
Python module to read, manipulate, and write Assimilate Scratch custom-command XML files.

### Description
The _scratchXML_ module converts an XML hierarchy output by [Assimilate Scratch](https://www.assimilateinc.com/products/) into an object based hierarchy.
It defines `Scratch`, `Construct`, `Slot`, and `Shot` classes that closely mirror the XML.

The typical use case is in support of a Scratch [Custom Command](https://www.assimilatesupport.com/akb/KnowledgebaseArticle51000.aspx).
Invoking the custom command causes Scratch to export XML, run your script, and then ingest the output. 
Within your script, the XML is read when the Scratch() object is created.  You now manipulate the hierarchy, then write out the result.

The scratchXML module refactors the XML output into the corresponding hierarchy of ScratchElement instances.
The resulting data can be easily examined using in a dictionary or attribute approach, e.g. `shot['length']` or `shot.length`.
Elements that are inline, e.g. the `uuid` in <shot uuid='123456789123456789'> are imported and accessible as `shot['@uuid']` or `shot.uuid`.
You can also create Scratch timelines from -- scratch, then output the XML and read them into Scratch.


### Installing
- ```pip install git+https://github.com/antoinedurr/ScratchXML```
### Dependencies
- [xmltodict](https://pypi.org/project/xmltodict) - convert XML into a dictionary

### Module
The [scratchXML module](https://github.com/antoinedurr/ScratchXML/tree/main/scratchXML) exports the following classes and functions:
- `Scratch` - the main entry point to creating a navigable dictionary hierarchy from XML output by Scratch
- `Group`, `Construct`, `Slot`, `Shot` - the elements that make up the dictionary hierarcy
- `scratchparse` - an Argparse overlay class that makes custom-command parsing easy and consistent
- `shotinfo` - a convenience SimpleNamespace overlay for storing arbitrary attributes of a shot

### Getting Started
The most typical use case is to process XML output by Scratch.  The `Scratch` class supports reading and writing the custom-command XML.  Upon reading the XML, it converts it to a dictionary (using xmltodict), and then reworks the hierarchy to turn the list of constructs into a list of actual `Construct` objects, which then contains a list of `Slot` objects, each of which has zero or more `Shot` objects.
```
from scratchXML import Scratch        # import the only thing we actually need

# read example1.xml and convert into a Scratch() hierarchy
scratch = Scratch(xml='xml/example1.xml')

# iterate our way down the hierarchy
for construct in scratch.constructs:  # iterate through all the constructs
  for slot in construct.slots:        # iterate through all the slots
    for shot in slot.shots:           # finally, iterate through all the shots
      print(f"Shot: {shot.name} slot: {shot.slot} layer: {shot.layer} file: {shot.file}")
```
Information on objects can be read as attributes or dictionary elements (shot['name'] == shot.name).  However, they currently can only be updated as dictionary elements.

Please see the full [getting-started tutorial](https://github.com/antoinedurr/ScratchXML/tree/main/getting_started).  This has a progression of examples that will make using the module clear, as well as exemplify the utilities that make writing Assimilate Scratch custom commands quick and easy.  Test .xml files are also included.

### Examples
The [working examples](https://github.com/antoinedurr/ScratchXML/tree/main/examples) folder contains some fully working Scratch custom commands.

- **scratch_export_csv.py** -- writes out shot info and (optionally) metadata to a .csv file and opens file
- **scratch_playlist2copypaste.py** -- grabs the bottom row of shots and puts the filepaths into the copy/paste buffer

See the Assimilate Scratch Docs for [how to install](https://www.assimilatesupport.com/akb/KnowledgebaseArticle51000.aspx) the custom command into Scratch.

### Limitations
- As of December 2025, only Timeline and Group exports are handled.  These can be with or without selected shots.
- Most attributes need to be modified using dictionary updates, e.g. shot['MOS'] = "N", not shot.MOS = "N".
- Scratch XML doesn't contain the _entire_ project.  For example, only base grades are included, grading layers are not
- when reading XML back in, Scratch won't automatically rearrange shots -- it's really only designed to modify shots in place.  The solution to this is to manually import the output XML into Scratch and delete the old construct(s).
