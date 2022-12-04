#!/usr/bin/env python3


from pathlib import Path

input = Path("input").read_text().splitlines()



kamien = ["A", "X"]
papier = ["B", "Y"]
nozyce = ["C", "Z"]

punkty = {
    "A": 1,
    "B": 2,
    "C": 3,
}

win = "Z"
draw = "Y"
lose = "X"


def lower(a):
    if a != "A":
        return chr(ord(a) - 1)
    return "C"


def higher(a):
    if a != "C":
        return chr(ord(a) + 1)
    return "A"


def beats(xyz, abc):
    return xyz == win


def f(a, x):
    if x == draw:
        return a
    if x == lose:
        return lower(a)
    if x == win:
        return higher(a)


s = 0
for x in input:
    if x == "":
        continue
    a, x = x.split()

    twoj_ruch = f(a, x)
    s += punkty[twoj_ruch]
    
    if x == draw:
        s += 3
    
    if beats(x, a):
        s += 6
print(s)