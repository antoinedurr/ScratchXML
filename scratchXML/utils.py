#!/usr/local/bin/python3
#
# A library for Assimilate Scratch
#
import sys

from types import SimpleNamespace
import argparse


class shotinfo(SimpleNamespace):
    pass  # convenient namespace for shot data


def parseargs(usage="", wait_til_finished=True, xml_export="Timeline", require_shot_selection=False):
    '''
    Argparse helper to parse common Scratch custom command arguments.
    Parameters:
        usage (str): Usage string for the script.  Succinctly tell the user what this custom command does.
        wait_til_finished (bool): Whether to include output XML argument.
        xml_export (str): Type of XML export in Scratch (Timeline, Group, Project, Selection) 
            N.B. only Timeline supported at this time.
        require_shot_selection (bool): Whether to indicate that shot selection is required.
    '''

    epilog = f'''
Scratch custom command settings:
    Type: Application
    Wait till Finished: {"On" if wait_til_finished else "Off"}
    XML Export: {xml_export}
    Require Shot Selection: {"On" if require_shot_selection else "Off"}
'''

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=epilog,
                                     description=usage)

    # for sure we always have an input XML
    parser.add_argument('inputxml', metavar='<input XML>')

    if wait_til_finished:
        # but if we turn on wait_til_finished, then we also get an output xml
        parser.add_argument('outputxml', metavar='<output XML>')

    # this is a hack to get around that Scratch seems to add an empty string as additional arg
    if sys.argv[-1] == '':
        sys.argv = sys.argv[0:-1]

    return parser
