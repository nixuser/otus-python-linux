import os
import sys
import stat

if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]

# Determine what permissions are already set using stat
permissions = stat.S_IMODE(os.stat(filename).st_mode)

if not os.access(filename, os.X_OK):
    print('Adding execute permission')
    new_permissions = permissions | stat.S_IXUSR
else:
    print('Removing execute permission')
    # use xor to remove the user execute permission
    new_permissions = permissions ^ stat.S_IXUSR

os.chmod(filename, new_permissions)

print('Readable:', os.access(filename, os.R_OK))
print('Writable:', os.access(filename, os.W_OK))
print('Executable:', os.access(filename, os.X_OK))