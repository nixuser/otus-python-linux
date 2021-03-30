import sys
import pprint

pprint.pprint(f'Default paths: {sys.path}')
try:
    from module_1 import name
except ModuleNotFoundError as e:
    print(e)
sys.path.append('/Users/agridyaev/OTUS/python_linux/pack')
pprint.pprint(f'Updated paths: {sys.path}')
from module_1 import name
print(name())
