#!/usr/local/bin/python3
#
# A library for Assimilate Scratch
#
import sys, os
import re
from pathlib import Path
import pprint
from types import SimpleNamespace
import pyperclip

from scratchXML import Scratch
from scratchXML import scratchparse

def main():
    '''
Scratch Custom Command to place the playlist filepaths into the copy/paste buffer.

The default behavior is to grab all the bottom row shots in the timeline.  However, if there
are any selected shots, only those selected shots will be placed into the copy/paste buffer.

This frame number on files will be replace with '.####.', e.g. foo.1001.exr -> foo.####.exr
    '''

    parser = scratchparse(usage=main.__doc__, require_shot_selection=False, wait_til_finished=False)
    args = parser.parse_args()

    WOTW_regex = '([A-Z]\d\d\d_[A-Z]\d\d\d_x\d\d+)'
    
    scratch = Scratch(xml=args.inputxml)

    class shotinfo(SimpleNamespace): pass # convenient namespace for selected and vfxslots
    
    # we shouldn't be getting any groups and just one construct
    construct = scratch.constructs[0]
    bottomshots = construct.shots(bottom_row=True)
    selectedshots = construct.shots(selected=True)

    # we default to the bottom row of shots, but if there are any selected shots, use those instead
    shots = selectedshots if len(selectedshots) > 0 else bottomshots

    # iterate through slots and shots to build shotlist
    shotlist = []
    for shot in shots:
        shotdata = shotinfo(slotindex=shot.slot, vfxname=shot.shotname(WOTW_regex), length=shot.length, name=shot.name, path=shot.file)
        shotdata.path = re.sub('\.\d\d\d\d+\.(\w+)', r'.####.\1', shotdata.path)
        shotlist.append(shotdata)
        
    playlist = '\n'.join([shot.path for shot in shotlist])

    pyperclip.copy(playlist)


if __name__ == "__main__":
    main()
    