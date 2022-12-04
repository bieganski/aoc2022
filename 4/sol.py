#!/usr/bin/env python3


from pathlib import Path

input = Path("input").read_text().splitlines()
input = [x for x in input if x != ""]


s = 0

for x in input:
    a, b = x.split(",")
    mina, maxa = list(map(int, a.split("-")))
    minb, maxb = list(map(int, b.split("-")))

    t1 = (mina, maxa)
    t2 = (minb, maxb)

    r1 = range(mina, maxa + 1, 1)
    r2 = range(minb, maxb + 1, 1)
    
    if mina in r2 and maxa in r2:
        s += 1
    elif minb in r1 and maxb in r1:
        s += 1

print(s)