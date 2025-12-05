#!/usr/local/bin/python3
#
# A library for Assimilate Scratch
#
import sys

from types import SimpleNamespace
import argparse


class shotinfo(SimpleNamespace):
    pass  # convenient namespace for shot data

class scratchargs(SimpleNamespace): pass

class scratchparse(argparse.ArgumentParser):
    '''
    Argparse helper to parse common Scratch custom command arguments.  Adds an input-xml and an optional output-xml argument.

    Parameters:
        usage (str): Usage string for the script.  Succinctly tell the user what this custom command does.
        wait_til_finished (bool): Whether to include output XML argument.
        xml_export (str): Type of XML export in Scratch (Timeline, Group, Project, Selection)
            N.B. only Timeline supported at this time.
        require_shot_selection (bool): Whether to indicate that shot selection is required.
    '''

    def __init__(self, usage="", wait_til_finished=True, xml_export="Timeline", require_shot_selection=False):

        epilog = f'''
Scratch custom command settings:
    Type: Application
    Wait till Finished: {"On" if wait_til_finished else "Off"}
    XML Export: {xml_export}
    Require Shot Selection: {"On" if require_shot_selection else "Off"}
'''
        super().__init__(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=epilog,
                                     description=usage)

        # for sure we always have an input XML
        super().add_argument('inputxml', metavar='<input XML>')
        if wait_til_finished:
            # but if we turn on wait_til_finished, then we also get an output xml
            super().add_argument('outputxml', metavar='<output XML>')

        # this is a hack to get around that Scratch seems to add an empty string as additional arg
        # if sys.argv[-1] == '':
        #     sys.argv = sys.argv[0:-1]

    def add_argument(self, *args, **kwargs):
        '''
        Overlay of add_argument that appends to the epilog
        '''
        super().add_argument(*args, **kwargs)
        # -pos <position=bottom> : [bottom, top]

        # name metavar [choice, choice (default)]
        
        name = args[0]
        if name == "-h":
            return
        
        ecomponents = [name]

        if 'metavar' in kwargs:
            ecomponents.append(kwargs['metavar'])
           
            if 'default' in kwargs or 'choices' in kwargs:
                ecomponents.append(':')

            if 'choices' in kwargs:
                choices = kwargs['choices']
                ecomponents.append(str(choices))

            if 'default' in kwargs:
                default = kwargs['default']
                ecomponents.append(f"({default})")
                
        estring = ' '.join(ecomponents)

        if 'Additional parameters' not in self.epilog:
            self.epilog += f"    Additional parameters: {estring}\n"
        else:
            self.epilog += f"                           {estring}\n"


    def parse_args(self, args=None, namespace=None):
        '''
        Overlay of parse_args to handle Scratch's quirk of adding an empty string as last argument.
        Also prints out some debug info to stderr.
        '''
        command = sys.argv[0]
        if args is None:
            args = sys.argv[1:]
        if len(args) > 0 and args[-1] == '':
            args = args[0:-1]
        parsedargs = super().parse_args(args, namespace)
    
        print("scratchXML:", command, parsedargs.inputxml, parsedargs.outputxml if hasattr(parsedargs, 'outputxml') else '', file=sys.stderr)

        return scratchargs(**vars(parsedargs))

