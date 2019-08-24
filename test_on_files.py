import os
import pathlib
import sys
import argparse

parser = argparse.ArgumentParser(description="Run epp -v on multiple files.")
parser.add_argument("directory", help="every *.cpp file from here will be tested")
parser.add_argument("start", type=int, nargs="?", default=0, help="start from i-th file, indexing from 0")
parser.add_argument("stop", type=int, nargs="?", default=None, help="stop at i-th file, indexing from 0")
parser.add_argument("-r", action="store_true", help="pass -r")

args = parser.parse_args()

paths = list(pathlib.Path(args.directory).glob("*.cpp"))

for f in paths[args.start:args.stop + 1 if args.stop else len(paths)]:
    print("===", f, "===")
    s = os.system(f"python epp.py {f} __b.cpp -v" + ("r" if args.r else ""))
    if s != 0:
        if s == 66:
            print(pathlib.Path("__a.cpp").read_text())
        print(f"Exited with code {s}")
        sys.exit(s)
