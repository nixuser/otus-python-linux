import os
import platform

print('Hardware info')
hw_details = (
    f"{platform.node()} "
    f"{platform.processor()} "
    f"{os.cpu_count()} "
)
print(hw_details)

print('Operating system:')
os_details = ( 
    f"{platform.system()} " 
    f"{platform.release()} " 
    f"{platform.version()} "
)
print(os_details)
print(platform.platform())

uname = platform.uname()
print(uname)
print(uname.release)
print(uname.system)