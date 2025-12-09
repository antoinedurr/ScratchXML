### Getting Started Examples

This examples in this folder are in support of the main page's README's examples section. 

#### **scratch_example1.py** 
The example1.py script reads an xml file created with a Timeline export from within Scratch.  Internally it recreates the hierarchy, then iterates through the shots in the timeline printing information about each shot.  This is the most basic of examples of getting information from your shots.
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

