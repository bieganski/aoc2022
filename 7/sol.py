#!/usr/bin/env python3


from pathlib import Path

input = Path("input").read_text().splitlines()

input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".splitlines()
input : list[str] = [x for x in input if x != ""]


from dataclasses import dataclass


@dataclass
class Node:
    name: str
    size: int = None
    
    @property
    def is_dir(self):
        return self.size is None


@dataclass
class Cmd:
    nodes : list[Node]
    is_ls : bool
    cd_where: str

assert input[0] == "$ cd /", f"xxx{input[0]}xxx"
cur_dir = Path("/")
input = input[1:]


a : list[Cmd] = []
for x in input:
    if x.startswith("$"):
        s = x.split()
        is_ls = s[1] == "ls"
        cmd = Cmd(
            nodes=[],
            is_ls=is_ls,
            cd_where=None if is_ls else s[2]
        )
        a.append(cmd)
    else:
        s = x.split()
        cmd : Cmd = a[-1]
        is_dir = s[0] == "dir"
        if is_dir:
            node = Node(name=s[1])
        else:
            node = Node(size=int(s[0]), name=s[1])
        cmd.nodes.append(node)

from pprint import pprint
pprint(a)

from collections import defaultdict
res = defaultdict(list)

for cmd in a:
    match cmd:
        case Cmd(is_ls=True):
            for node in cmd.nodes:
                match node:
                    case Node(is_dir=True):
                        pass
                    case Node(is_dir=False):
                        res[cur_dir].append(node.size)
        case Cmd(is_ls=False):
            print("cd")
            cur_dir = (cur_dir / cmd.cd_where).resolve() # !!!

pprint(res)
s = 0
for k, v in res.items():
    ss = sum(v)
    print(k, ss)
    if ss <= 100_000:
        s += ss
print(s)