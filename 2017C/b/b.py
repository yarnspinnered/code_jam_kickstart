import logging
import re
from pprint import pprint
from collections import Counter
logging.basicConfig(level=logging.ERROR)

def input(file_name):
    res = []
    with open(file_name) as file:
        lines = file.__iter__()
        next = lambda: lines.__next__()

        n = int(next().strip())  # Number of cases
        for i in range(n):
            m = int(next().strip())  # Number of lines for this case
            res.append([[x for x in next().strip()] for _ in range(m)])
    # pprint(res)
    return res

def output(arr, file_name):
    with open(file_name, 'w') as f:
        for i,v in enumerate(arr):
            f.write("Case #{}: ".format(i + 1) + ('POSSIBLE' if v else 'IMPOSSIBLE') + '\n')

def positions_of_X(line):
    res = []
    for i,c in enumerate(line):
        if c == 'X':
            res.append(i)
    return tuple(res)

def solve(arr):
    # pprint(arr)
    single_count = 0
    single_col = None
    d = {}
    for line in arr:
        key = positions_of_X(line)
        if len(key) == 1:
            single_count += 1
            single_col = key[0]
        else:
            if key in d:

                d[key] = d[key] +  1
            else:
                d[key] = 1
    for k,v in d.items():
        if v != 2:
            return False
    if single_count != 1:
        return False

    single_count = 0
    for r in arr:
        if r[single_col] == 'X':
            single_count += 1
    if single_count > 1:
        return False
    return True

small_input = input('B-small-practice.in')
output([solve(x) for x in small_input], 'B-small-practice.out')

large_input = input('B-large-practice.in')
output([solve(x) for x in large_input], 'B-large-practice.out')