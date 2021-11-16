import sys

with open(sys.argv[1], "r") as fh:
    lines = fh.readlines()

for line in lines:
    line = line.strip()
    if line.startwith(">"):
        header = line
    else:
        length = len(line)
        print(length, header)
