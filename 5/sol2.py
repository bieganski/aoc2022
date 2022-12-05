#!/usr/bin/env python3


from pathlib import Path

input = Path("input").read_text().splitlines()


# input = """
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# """.splitlines()

input = [x for x in input if x != ""]


moves = [i for i, x in enumerate(input) if "move" in x]
moves_first_idx = moves[0]

max_line = input[moves_first_idx - 1]
max_stack = int(max_line.split()[-1])

draw = input[:moves_first_idx - 1] # -1 because of that 'max_line' string.
moves = input[moves_first_idx:]

draw = [list(f"{x} ") for x in draw]

import numpy as np
draw = np.array(draw).reshape((-1, max_stack, 4))



stacks = [[] for _ in range(max_stack)]
draw = np.flip(draw, axis=0)

assert draw.shape[1] == max_stack, (draw.shape, max_stack)

# construct stack.
for idx in np.ndindex(draw.shape[:2]):
    row_idx, stack_idx = idx
    from operator import __add__
    from functools import reduce
    four = reduce(__add__, draw[row_idx, stack_idx]) # construct back string.
    if four == "    ":
        continue
    letter :str = four[1]
    assert letter.isupper()
    stacks[stack_idx].append(letter)


for x in moves:
    # move 1 from 2 to 1
    _, num, _, _from, _, _to = x.split()
    num = int(num)
    _from = int(_from) - 1
    _to = int(_to) - 1
    
    tmp = []
    for _ in range(num):
        val = stacks[_from].pop() 
        tmp.append(val)
    
    while tmp:
        stacks[_to].append(tmp.pop())

res = [x.pop() for x in stacks]
print(reduce(__add__, res))