import re

file = open("inputs/14.in")
mem_regex = re.compile("mem\\[([0-9]+)] = ([0-9]+)")
mask_ones = 1
mask_zeros = 0
mem = {}
for line in file:
    if line.startswith("mask = "):
        mask = line[7:-1]
        mask_ones = int(mask.replace('X', '0'), 2)
        mask_zeros = int(mask.replace('X', '1'), 2)
    else:
        (index, value) = mem_regex.match(line).groups()
        mem[int(index)] = (int(value) | mask_ones) & mask_zeros
print(sum(mem.values()))


file.seek(0)
mask_x = 1
mem = {}
masks = []
for line in file:
    if line.startswith("mask = "):
        mask = line[7:-1]
        mask_x = int(mask.replace('0', '1').replace('X', '0'), 2)
        masks = [int(mask.replace('X', '0'), 2)]
        for i, c in enumerate(mask):
            if c == 'X':
                new_masks = []
                for r in masks:
                    new_masks.append(r)
                    new_masks.append(r + pow(2, len(mask) - i - 1))
                masks = new_masks
    else:
        (index, value) = mem_regex.match(line).groups()
        for m in masks:
            index = int(index) & mask_x | m
            mem[index] = int(value)
print(sum(mem.values()))
