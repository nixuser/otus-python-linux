"""
pip install psutil
"""

import psutil
from pprint import pprint
mem = psutil.virtual_memory()
print(mem)
pprint(
    psutil.net_connections()
)
pprint(
    psutil.net_if_addrs()
)