"""
Usage examples:
echo test_string | python3 01_sys_stdin.py
yes | head -10 | python3 01_sys_stdin.py
python3 01_sys_stdin.py < 01_sys_stdin.py
"""

import sys


for line in sys.stdin:
    print(line.strip())

