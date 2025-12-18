#!/usr/bin/env python3
#
# https://github.com/antoinedurr/ScratchXML/blob/main/getting_started/scratch_example4.py
# Print out metadata on each shot
#
from scratchXML import Scratch
from scratchXML import scratchparse  # Argparse subclass specific to ScratchXML 
import pprint

parser = scratchparse(usage="Print out info for each shot, including metadata dict", wait_til_finished=False)
args = parser.parse_args()

# ‘inputxml’ is the standard args attribute for the XML that Scratch writes out to Temp
scratch = Scratch(xml=args.inputxml)
timeline = scratch.constructs[0]

# get the selected shots, or if none were selected, get all shots
shots = timeline.shots(selected=True) or timeline.shots()

for shot in shots:
   # print out metadata for each shot
   print(f"Shot: {shot.name} Slot: {shot.slot} Layer: {shot.layer} Metadata:\n{pprint.pformat(shot.metadata, indent=4)}")
   shot.metadata['example_key'] = 'example_value'  # modify metadata example

# scratch['@action'] = "update"
scratch['@action'] = "update" # options are: udate, append, insert, 

scratch.write(xml=args.outputxml)
