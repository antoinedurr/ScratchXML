#!/usr/bin/env python3
#
# https://github.com/antoinedurr/ScratchXML/blob/main/getting_started/scratch_example1.py
# A simple example showing how to read a Scratch XML file

from scratchXML import Scratch

# read example1.xml and convert into a Scratch() hierarchy
scratch = Scratch(xml='xml/example1.xml')

# iterate through all the constructs (there will be only one)
for construct in scratch.constructs:
  for slot in construct.slots:  # iterate through all the slots
    for shot in slot.shots:  # finally, iterate through all the shots
      # print out metadata for each shot
      print(
          f"Shot: {shot.name} slot: {shot.slot} layer: {shot.layer} file: {shot.file}")
