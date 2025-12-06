#!/usr/local/bin/python3
#
# scratch_playlist2copypaste.py -- Scratch Custom Command to place the playlist filepaths into the copy/paste buffer.
#
import sys, os
import re
from pathlib import Path
import pprint
from types import SimpleNamespace
import pyperclip

from scratchXML import Scratch
from scratchXML import scratchparse, shotinfo

def main():
    '''
    Scratch Custom Command to place the playlist filepaths into the copy/paste buffer.

    The default behavior is to grab all the bottom row shots in the timeline.  However, if there
    are any selected shots, only those selected shots will be placed into the copy/paste buffer.

    This frame number on files will be replace with '.####.', e.g. foo.1001.exr -> foo.####.exr
    '''

    parser = scratchparse(usage=main.__doc__, require_shot_selection=False, wait_til_finished=False)
    args = parser.parse_args()

    VFX_regex = '([A-Z]\d\d\d_[A-Z]\d\d\d_x\d\d+)' # shot names are e.g. A001_C004_x10 i.e. camera+roll+x##
    
    # we shouldn't be getting any groups and just the one construct
    timeline = Scratch(xml=args.inputxml).constructs[0]

    # if no selected shots use the bottom row by default
    shots = timeline.shots(selected=True) or timeline.shots(bottom_row=True)

    # iterate through slots and shots to build shotlist
    shotlist = []
    for shot in shots:
        shotdata = shotinfo(slotindex=shot.slot, vfxname=shot.shotname(VFX_regex), length=shot.length, name=shot.name, path=shot.file)
        shotdata.path = re.sub('\.\d\d\d\d+\.(\w+)', r'.####.\1', shotdata.path)
        shotlist.append(shotdata)
        
    playlist = '\n'.join([shot.path for shot in shotlist])

    pyperclip.copy(playlist)


if __name__ == "__main__":
    main()
    