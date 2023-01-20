"""
python3 03_args.py -h
python3 03_args.py --dir /etc/
python3 03_args.py -v --dir test_dir
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="Directory to list files")
parser.add_argument("-v", "--verbosity", help="increase output verbosity", 
                    action="store_true")
args = parser.parse_args()
print(args.dir)
print(args.verbosity)

