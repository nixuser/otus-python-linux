"""
fileinput can read files passed as command line arguments

Usage examples:
python3 03_fileinput_from_args.py 01_sys_stdin.py 02_fileinput.py
"""

import fileinput

for line in fileinput.input():
    if fileinput.isfirstline():
	    print(fileinput.filename())
    print(line.strip())
    #print(fileinput.filelineno())
