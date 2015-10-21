import sys
import re


with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        a = re.sub(r'[^a-z]+', ' ', line.lower())
        if a[0] == ' ':
            print a[1:]
        else:
            print a
