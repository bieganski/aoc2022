#!/usr/bin/env python3


from pathlib import Path

input = Path("input").read_text().splitlines()


_max = 0
global_max = 0
lst = []
cur = 0
for x in input:
    if x == "":
        lst.append(cur)
        cur = 0
    else:
        cur += int(x)

lst =sorted(lst, reverse=True)
print(sum(lst[:3]))
