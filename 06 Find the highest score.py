__author__ = 'ShinChan'

import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        groups = line.replace('\n','').split(' | ')
        g_len = len(groups)
        highs = groups[0].split(' ')
        for group in groups[1:]:
            numbers = group.split(' ')
            for i in xrange(0, len(numbers)):
                if int(numbers[i]) > int(highs[i]):
                    highs[i] = numbers[i]
        print ' '.join(highs)
