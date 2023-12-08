import math
import re
from itertools import cycle

pattern = r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)"
net = dict()
with open("input8.txt") as f:
    inst = f.readline().strip()
    next(f)
    for line in f:
        k, *v = re.fullmatch(pattern, line.rstrip()).groups()
        net[k] = v


def count_steps(pattern, node):
    for i, lr_idx in enumerate(cycle(map("LR".index, inst)), start=1):
        node = net[node][lr_idx]
        if re.fullmatch(pattern, node):
            return i


# Part 1
p1 = count_steps("ZZZ", "AAA")
print(f"Part 1: {p1}")

# Part 2
_node_iter = filter(lambda node: re.fullmatch("[A-Z]{2}A", node), net.keys())
p2 = math.lcm(*(count_steps("[A-Z]{2}Z", node) for node in _node_iter))
print(f"Part 2: {p2}")