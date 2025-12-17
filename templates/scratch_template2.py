#!/usr/bin/env python3
#
# https://github.com/antoinedurr/ScratchXML/blob/main/getting_started/scratch_example4.py
# Print out metadata on each shot
#
from scratchXML import Scratch
from scratchXML import scratchparse  # Argparse subclass specific to ScratchXML
import pprint

parser = scratchparse(
    usage="Print out info for each shot, including metadata dict", wait_til_finished=False)
args = parser.parse_args()

# ‘inputxml’ is the standard args attribute for the XML that Scratch writes out to Temp
scratch = Scratch(xml=args.inputxml)
timeline = scratch.constructs[0]

# get the selected shots, or if none were selected, get all shots
shots = timeline.shots(selected=None) or timeline.shots()

for slot in timeline.slots:
    print(f"Slot: {slot.index}")
    if slot.shots:
        baselength = slot.shots[0].length
        for shot in slot.shots[1:]:
            if shot.length != baselength:
                print(f"  Length mismatch in '{shot.name}' layer {shot.layer} has length {shot.length}, expected {baselength}")        
