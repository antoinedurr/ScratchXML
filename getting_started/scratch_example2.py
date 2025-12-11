#!/usr/bin/env python3
#
# https://github.com/antoinedurr/ScratchXML/blob/main/getting_started/scratch_example2.py
# A simpler way to iterate through the shots
#
from scratchXML import Scratch
import pprint

# read example2.xml and convert into a Scratch() hierarchy
scratch = Scratch(xml='xml/example2.xml')

# iterate through all the shots, assuming a single timeline
for shot in scratch.constructs[0].shots(selected=True):  # only selected shots
  print(f"Shot: {shot.name} slot: {shot.slot} layer: {shot.layer} file: {shot.file}")
  # pprint.pprint(shot.metadata) # uncomment to pretty-print the metadata dictionary
