class Cube:
    def __init__(self, x, y, z, w = 0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_neighbour(self, other):
        if self == other:
            return False
        x_diff = abs(self.x - other.x)
        y_diff = abs(self.y - other.y)
        z_diff = abs(self.z - other.z)
        w_diff = abs(self.w - other.w)
        return x_diff <= 1 and y_diff <= 1 and z_diff <= 1 and w_diff <= 1

    def flipped_by_z(self):
        return Cube(self.x, self.y, -self.z, self.w)

    def flipped_by_w(self):
        return Cube(self.x, self.y, self.z, -self.w)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w


def bounds_of(cubes):
    bounds = [(0, 0), (0, 0), (0, 0), (0, 0)]
    for c in cubes:
        bounds[0] = (min(c.x - 1, bounds[0][0]), max(c.x + 1, bounds[0][1]))
        bounds[1] = (min(c.y - 1, bounds[1][0]), max(c.y + 1, bounds[1][1]))
        bounds[2] = (min(c.z - 1, bounds[2][0]), max(c.z + 1, bounds[2][1]))
        bounds[3] = (min(c.w - 1, bounds[3][0]), max(c.w + 1, bounds[3][1]))
    return bounds


file = open("inputs/17.in")
cubes = []
for row, line in enumerate(file):
    for column, character in enumerate(line):
        if character == '#':
            cubes.append(Cube(column, row, 0))
original_cubes = cubes

for _ in range(6):
    bounds = bounds_of(cubes)
    new_cubes = []
    for x in range(bounds[0][0], bounds[0][1] + 1):
        for y in range(bounds[1][0], bounds[1][1] + 1):
            for z in range(bounds[2][0], bounds[2][1] + 1):
                neighbors = 0
                maybe_active = Cube(x, y, z)
                for c in cubes:
                    if maybe_active.is_neighbour(c):
                        neighbors += 1
                if neighbors == 3:
                    new_cubes.append(maybe_active)
    for c1 in cubes:
        neighbors = 0
        for c2 in cubes:
            if c1.is_neighbour(c2):
                neighbors += 1
        if neighbors == 2 or neighbors == 3 and c1 not in new_cubes:
            new_cubes.append(c1)
    cubes = new_cubes

print(len(cubes))

cubes = original_cubes
for i in range(6):
    bounds = bounds_of(cubes)
    new_cubes = []
    for x in range(bounds[0][0], bounds[0][1] + 1):
        for y in range(bounds[1][0], bounds[1][1] + 1):
            for z in range(bounds[2][0], bounds[2][1] + 1):
                for w in range(bounds[3][0], bounds[3][1] + 1):
                    neighbors = 0
                    maybe_active = Cube(x, y, z, w)
                    for c in cubes:
                        if maybe_active.is_neighbour(c):
                            neighbors += 1
                    if neighbors == 3:
                        new_cubes.append(maybe_active)
    for c1 in cubes:
        neighbors = 0
        for c2 in cubes:
            if c1.is_neighbour(c2):
                neighbors += 1
        if neighbors == 2 or neighbors == 3 and c1 not in new_cubes:
            new_cubes.append(c1)
    cubes = new_cubes

print(len(cubes))
