#!/usr/bin/env python3
#
# https://github.com/antoinedurr/ScratchXML/blob/main/getting_started/scratch_example3.py
# Reverse the order of shots in each slot
#
from scratchXML import Scratch

# read example3.xml and convert into a Scratch() hierarchy
scratch = Scratch(xml='xml/example3.xml')

print([shot.name for shot in scratch.constructs[0].slots[0].shots])  # before reversal

for construct in scratch.constructs:
  for slot in construct.slots:
    slot.shots = reversed(slot.shots)  # see limitations

print([shot.name for shot in scratch.constructs[0].slots[0].shots]) # after reversal

scratch['@update'] = "Y"               # tell Scratch to update from the resulting xml
scratch.write('xml/output.xml')        # write out resulting file
