#!/usr/local/bin/python3
#
# https://github.com/antoinedurr/ScratchXML/blob/main/examples/scratch_find_length_mismatches.py
# Example Assimilate Scratch custom command that finds length mismatches between different versions
# of shots within slots.  It prints out the results to stderr and pops up a message box with the results.
# 
# Copyright(c) 2025 Antoine Durr
# antoine@antoinedurr.com
#
import sys
from scratchXML import Scratch
from scratchXML import scratchparse, scratchmessage

parser = scratchparse(usage="Print out info for each shot, including metadata dict", wait_til_finished=False)
args = parser.parse_args()

# ‘inputxml’ is the standard args attribute for the XML that Scratch writes out to Temp
scratch = Scratch(xml=args.inputxml)
timeline = scratch.constructs[0]

# get the selected shots, or if none were selected, get all shots
shots = timeline.shots(selected=None) or timeline.shots()

mismatches = 0
message = ""
for slot in timeline.slots: # iterate through slots
    if slot.shots: # skip empty slots
        baselength = slot.shots[0].length # length of version 0
        for shot in slot.shots[1:]: # iterate through remaining versions above
            if shot.length != baselength:
                message += f"Slot {slot.index} [{baselength}f] version {shot.layer}: {shot.length}f\n"
                mismatches += 1


if mismatches == 0:
    message = f"No length mismatches found in any of the {len(timeline.slots)} slots"

print(message, file=sys.stderr)
scratchmessage(message, "Find Length Mismatches")
