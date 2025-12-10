### Getting Started Examples & Tuturial

This examples in this folder are in support of the main page's README's examples section. The files (unlike the code excerpts below) start "at the top" with the proper imports.

#### [Example 1](https://github.com/antoinedurr/ScratchXML/blob/main/getting_started/scratch_example1.py) - Print Shot Info
The example1.py script reads an xml file created with a Timeline export from within Scratch.  Internally it recreates the hierarchy, then iterates through the shots in the timeline printing information about each shot.  This is the most basic of examples of getting information from your shots.
```
from scratchXML import Scratch

# read example1.xml and convert into a Scratch() hierarchy
scratch = Scratch(xml='xml/example1.xml')

# iterate through all the constructs (there will be only one) and print out shot info
for construct in scratch.constructs:  # likely to be only one construct if export was 'Timeline'
  for slot in construct.slots:        # iterate through all the slots
    for shot in slot.shots:           # finally, iterate through all the shots
      print(f"Shot: {shot.name} slot: {shot.slot} layer: {shot.layer} file: {shot.file}")
```
The expected output is as follows:
```
%> python3 scratch_example1.py xml/example1.xml
Shot: A192_C001_1123S9[1] slot: 0 layer: 0 file: /Volumes/ABCD/Media/RAWs/A192_C001_1123S9.RDC/A192_C001_1123S9_001.R3D
Shot: A110_C004_1015BJ[1] slot: 1 layer: 0 file: /Volumes/ABCD/Media/RAWs/A110_C004_1015BJ.RDC/A110_C004_1015BJ_001.R3D
Shot: A120_C001_1017EN[1] slot: 2 layer: 0 file: /Volumes/ABCD/Media/RAWs/A120_C001_1017EN.RDC/A120_C001_1017EN_001.R3D
Shot: A171_C022_1112RI[1] slot: 3 layer: 0 file: /Volumes/ABCD/Media/RAWs/A171_C022_1112RI.RDC/A171_C022_1112RI_001.R3D
Shot: B060_C004_1029E9[1] slot: 4 layer: 0 file: /Volumes/ABCD/Media/RAWs/B060_C004_1029E9.RDC/B060_C004_1029E9_001.R3D
```

#### [Example 2](https://github.com/antoinedurr/ScratchXML/blob/main/getting_started/scratch_example2.py) - Print Shot Info and metadata (easier way)
Needing a triple nested for-loop gets really old, thus use `Construct`'s `shots()` method.  `shots()` has some optional parameters
including 'selected' and 'bottom_row' which let you pick and choose what category of shots you want.  We're using selected
shots in this example.
```
for shot in scratch.constructs[0].shots(selected=True):  # only selected shots
  print(f"Shot: {shot.name} slot: {shot.slot} layer: {shot.layer} file: {shot.file}")
  # pprint.pprint(shot.metadata) # uncomment to pretty-print the metadata dictionary
```
Returning only the selected shots, you get this:
```
%> python3 scratch_example2.py
Shot: A192_C001_1123S9[1] slot: 0 layer: 0 file: /Volumes/ABCD/Media/RAWs/A192_C001_1123S9.RDC/A192_C001_1123S9_001.R3D
Shot: A110_C004_1015BJ[1] slot: 1 layer: 0 file: /Volumes/ABCD/Media/RAWs/A110_C004_1015BJ.RDC/A110_C004_1015BJ_001.R3D
```
The 'selected' parameter can take True (return only selected shots), False (return only non-selected shots), or None (return all shots).

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

