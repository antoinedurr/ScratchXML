### Working Examples

This folder contains various Assimilate Scratch custom-command real-world scripts.  N.B. they are a bit Mac centric at the moment (Dec 2025). 

- **scratch_export_csv.py**
  - This Python Scratch custom command script creates a .csv file with a line for each shot containing information about the shot.  If there are selected
shots, then the CSV will only contain those shots.
- **scratch_find_length_mismatches.py**
  - This custom command finds all shots on version 1 or above whose length doesn't match version 0.
  - This often happens in a VFX context where different versions of a comp are loaded and helps identify mismatches.   
- **scratch_playlist2copypaste.py**
  - Similar to the export_csv example, this Scratch custom command script collects the filepaths of all (or just the selected) shots and puts it 
into the copy-paste buffer using PyperClip.
