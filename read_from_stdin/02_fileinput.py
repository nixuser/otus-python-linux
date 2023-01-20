"""
Usage examples:
echo test_string | python3 02_fileinput.py
yes | head -10 | python3 02_fileinput.py
python3 02_fileinput.py < 02_fileinput.py
"""

import fileinput

for line in fileinput.input():
    print(line.strip())
