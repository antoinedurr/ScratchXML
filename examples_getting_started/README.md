### Getting Started Examples

This examples in this folder are in support of the main page's README's examples section. 

#### **scratch_example1.py** 
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
  - This Python Scratch custom command script creates a .csv file with a line for each shot containing information about the shot.  If there are selected
shots, then the CSV will only contain those shots.
