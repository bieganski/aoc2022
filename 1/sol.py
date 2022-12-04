#!/usr/bin/env python3


from pathlib import Path

input = Path("input").read_text().splitlines()


_max = 0
global_max = 0
for x in input:
    if x == "":
        _max = 0
    else:
        _max += int(x)
        global_max = max(_max, global_max)

print(global_max)
