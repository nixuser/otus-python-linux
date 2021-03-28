import os

file_path = 'os_lib/test_file.txt'
link_name = '/tmp/' + os.path.basename(file_path)

print('Creating link {} -> {}'.format(link_name, file_path))
os.symlink(file_path, link_name)

stat_info = os.lstat(link_name)
print(f'Permissions: {oct(stat_info.st_mode)}')
print(f'Points to: {os.readlink(link_name)}')

os.unlink(link_name)
