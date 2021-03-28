import os

dir_name = 'p_dir/ch_dir'

os.makedirs(dir_name)
ch2_dir = os.path.join(dir_name, 'ch2_dir')
os.mkdir(ch2_dir)

file_name = os.path.join(ch2_dir, 'example.txt')
with open(file_name, 'w') as f:
    f.write('Hello, OTUS!')

os.unlink(file_name)
os.rmdir(ch2_dir)
os.removedirs(dir_name)
