#!/usr/bin/env python3


from pathlib import Path

input = Path("input").read_text().splitlines()


# input = [
# "vJrwpWtwJgWrhcsFMMfFFhFp",
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
# "PmmdzqPrVvPwwTWBwg",
# "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
# "ttgJtRGJQctTZtZT",
# "CrZsJsPPZsGzwwsLwLmpwMDw",
# ]

_input = []

s = 0

for x in input:
    l = len(x) // 2
    a, b = (x[:l], x[l:])
    a, b = set(a), set(b)
    if len(a) == 0:
        continue
    common = a.intersection(b).pop()

    def val(x: str):
        if x.islower():
            return ord(x) - 96
        return ord(x) - 64 + 26

    # val = lambda x: ord(x) - 64 if x > "A" else ord(x) - 96
    n = val(common)
    print(common, n)
    s += n
    
print(s)