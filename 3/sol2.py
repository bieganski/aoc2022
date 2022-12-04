#!/usr/bin/env python3


from pathlib import Path

input = Path("input").read_text().splitlines()
input = [x for x in input if x != ""]


# input = [
# "vJrwpWtwJgWrhcsFMMfFFhFp",
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
# "PmmdzqPrVvPwwTWBwg",
# "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
# "ttgJtRGJQctTZtZT",
# "CrZsJsPPZsGzwwsLwLmpwMDw",
# ]

import numpy as np
input = np.array(input).reshape((-1, 3))

s = 0


def max_occurrences_2(seq):
    from collections import defaultdict
    from operator import itemgetter
    "defaultdict iteritems"
    c = defaultdict(int)
    for item in seq:
        c[item] += 1
    return max(c.items(), key=itemgetter(1))


for g in input:
    a,b,c = g

    a , b, c= set(a), set(b), set(c)

    common = a.intersection(b).intersection(c).pop()

    def val(x: str):
        if x.islower():
            return ord(x) - 96
        return ord(x) - 64 + 26

    # val = lambda x: ord(x) - 64 if x > "A" else ord(x) - 96
    n = val(common)
    print(common, n)
    s += n
    
print(s)