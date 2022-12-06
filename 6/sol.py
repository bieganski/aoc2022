#!/usr/bin/env python3


from pathlib import Path

input = Path("input").read_text().splitlines()


# input = """
# mjqjpqmgbljsphdztnvjfqwrcgsmlb
# """.splitlines()

input = [x for x in input if x != ""]


assert len(input) == 1
input = input[0]

n = 14
for x in range(n-1, len(input) - 1):
    if len(set(input[x-n:x])) == n:
        print(x)
        break