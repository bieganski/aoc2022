#!/usr/bin/env python3


from pathlib import Path

input = Path("input").read_text().splitlines()



kamien = ["A", "X"]
papier = ["B", "Y"]
nozyce = ["C", "Z"]

punkty = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def beats(xyz, abc):
    if (xyz == "X" and abc == "C") or (xyz == "Y" and abc == "A") or (xyz == "Z" and abc == "B"):
        return True
    return False


s = 0
for x in input:
    if x == "":
        continue
    a, x = x.split()
    s += punkty[x]
    if (a in kamien and x in kamien) or (a in papier and x in papier) or (a in nozyce and x in nozyce):
        s += 3
    elif beats(x, a):
        s += 6
print(s)