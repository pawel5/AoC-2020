coords = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
vals = [0, 0, 0, 0]
last = coords['E']
file = open("inputs/12.in")

for line in file:
    direction = line[0]
    amount = int(line[1:])
    if direction == 'F':
        vals[last] += amount
    elif direction == 'R':
        last = (last + amount // 90) % 4
    elif direction == 'L':
        last = (last - amount // 90) % 4
    else:
        vals[coords[direction]] += amount

print(abs(vals[0] - vals[2]) + abs(vals[1] - vals[3]))

file.seek(0)
vals = [0, 0, 0, 0]
waypoint = [1, 10, 0, 0]
last = coords['E']

for line in file:
    direction = line[0]
    amount = int(line[1:])
    if direction == 'F':
        for i in range(len(vals)):
            vals[i] += waypoint[i] * amount
    elif direction == 'R':
        for i in range(amount // 90):
            waypoint = [waypoint[-1]] + waypoint[0:3]
    elif direction == 'L':
        for i in range(amount // 90):
            waypoint = waypoint[1:] + [waypoint[0]]
    else:
        waypoint[coords[direction]] += amount

print(abs(vals[0] - vals[2]) + abs(vals[1] - vals[3]))
