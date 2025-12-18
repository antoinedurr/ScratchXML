#!/usr/bin/env python3
#
# https://github.com/antoinedurr/ScratchXML/blob/main/templates/scratch_template1.py
# scratchXML template to list info on selected shots (or all shots if none selected)
# arguments is only input XML file
#
from scratchXML import Scratch
from scratchXML import scratchparse  # Argparse subclass specific to ScratchXML
import pprint

parser = scratchparse(usage="Print info for each selected shot", wait_til_finished=False)
args = parser.parse_args()

# ‘inputxml’ is the standard args attribute for the XML that Scratch writes out to Temp
scratch = Scratch(xml=args.inputxml)
timeline = scratch.constructs[0]

# get the selected shots, or if none were selected, get all shots
shots = timeline.shots(selected=True) or timeline.shots()

# print out info for each shot
for shot in shots:
   print(f"Shot: {shot.name} Slot: {shot.slot} Layer: {shot.layer} Length: {shot.length} File: {shot.file}")
