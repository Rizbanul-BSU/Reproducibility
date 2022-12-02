import sys

path = sys.argv[1]

with open(path, encoding='utf8') as f:
    for line in f:
        print(line.strip())