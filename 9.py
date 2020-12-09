from itertools import combinations

preamble = 25
entries = [int(line) for line in open("inputs/9.in")]
start = 0
found = -1

while start+preamble < len(entries):
    products = [entry[0] + entry[1] for entry in combinations(entries[start:start+preamble], 2)]
    if not entries[start+preamble] in products:
        found = entries[start+preamble]
        break
    start += 1

print(found)

start = 0
rng = 1

while start+rng < len(entries):
    part = entries[start:start+rng]
    partial_sum = sum(part)
    if partial_sum == found:
        print(max(part) + min(part))
        break
    elif partial_sum > found:
        start += 1
        rng = 1
    else:
        rng += 1
