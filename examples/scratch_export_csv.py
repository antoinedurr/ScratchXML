#!/usr/local/bin/python3
#
# scratch_export_csv.py -- Scratch Custom Command to write .csv of the all shots' metadata.
# Copyright (C) 2025 Antoine Durr
# antoine@antoinedurr.com
#
import sys
import os

from pathlib import Path
import pprint
import csv
import pyperclip
import subprocess

from scratchXML import Scratch
from scratchXML import scratchparse, shotinfo


def main():
    '''
    Scratch Custom Command to write .csv of the all shots' metadata.  
    This will write it to the Scratch project Temp folder as <construct_name>.csv

    Once written, it calls 'open' on the csv file for viewing.  It also places the csv filepath into the copy/paste buffer.
    '''
    parser = scratchparse(usage=main.__doc__, require_shot_selection=False, wait_til_finished=False)
    parser.add_argument('-meta', action='store_true', help='Include all metadata keys in the CSV')
    args = parser.parse_args()

    # we shouldn't be getting any groups and just the one construct
    scratch = Scratch(xml=args.inputxml)
    timeline = scratch.constructs[0]

    # user can select some shots and it'll generate the csv for those only, else it'll generate it for all shots
    shots = timeline.shots(selected=True) or timeline.shots()

    metakeys = set()  # the set of all metadata keys across all shots
    shotlist = []  # the list of shots' shotinfo objects

    for shot in shots:
        metakeys.update(shot.metadata.keys())

        shotdata = shotinfo(slotindex=shot.slot, layer=shot.layer,
                            length=shot.length, name=shot.name, path=shot.file)
        if args.meta:
            shotdata.__dict__.update(shot.metadata)

        shotlist.append(shotdata)

    csvfile = Path(scratch.temp_path) / f"{timeline.name}.csv"

    with open(csvfile, mode='w', newline='') as csvfile:
        fieldnames = ['slotindex', 'layer', 'length', 'name', 'path']
        if args.meta:
            fieldnames += list(metakeys)

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for shot in shotlist:
            writer.writerow(shot.__dict__)

    print(f"Wrote {len(shotlist)} shots to {csvfile.name}", file=sys.stderr)
    pyperclip.copy("'" + csvfile.name + "'")
    subprocess.run(["open", csvfile.name])


if __name__ == "__main__":
    main()
