"""
fileinput can read files passed as command line arguments

Usage examples:
python3 04_fileinput_from_args_env.py 01_sys_stdin.py
LINENUM=yes python3 04_fileinput_from_args_env.py 01_sys_stdin.py

"""

import os
import fileinput

show_line_number = ''

if 'LINENUM' in os.environ and os.environ['LINENUM'] == 'yes':
        show_line_number = 'yes'
for line in fileinput.input():
    if fileinput.isfirstline():
	    print(fileinput.filename())
    content = line.strip()
    if show_line_number:
        content =  f" {fileinput.filelineno()} {line.strip()}"
    print(content)

