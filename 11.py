class Seats:
    def __init__(self, filename):
        self.seats = [line[:-1] for line in open(filename)]
        self.height = len(self.seats)
        self.width = len(self.seats[0])

    def occupied(self):
        occupied_sum = 0
        for row in self.seats:
            occupied_sum += row.count("#")
        return occupied_sum

    def simulate_near(self):
        new_seats = []
        changed = True
        while changed:
            changed = False
            for row in range(self.height):
                new_row = ""
                for col in range(self.width):
                    if self.seats[row][col] == '.':
                        new_state = '.'
                    elif self.seats[row][col] == 'L' and self.occupied_around(row, col) == 0:
                        new_state = '#'
                        changed = True
                    elif self.seats[row][col] == '#' and self.occupied_around(row, col) >= 4:
                        new_state = 'L'
                        changed = True
                    else:
                        new_state = self.seats[row][col]
                    new_row += new_state
                new_seats.append(new_row)
            self.seats = new_seats
            new_seats = []

    def occupied_around(self, y, x):
        occupied = 0
        for dy in range(y - 1, y + 2):
            if 0 <= dy < self.height:
                for dx in range(x - 1, x + 2):
                    if 0 <= dx < self.width:
                        if not (dy == y and dx == x) and self.seats[dy][dx] == '#':
                            occupied += 1
        return occupied

    def simulate_visible(self):
        new_seats = []
        changed = True
        while changed:
            changed = False
            for row in range(self.height):
                new_row = ""
                for col in range(self.width):
                    if self.seats[row][col] == '.':
                        new_state = '.'
                    elif self.seats[row][col] == 'L' and self.occupied_visible(row, col) == 0:
                        new_state = '#'
                        changed = True
                    elif self.seats[row][col] == '#' and self.occupied_visible(row, col) >= 5:
                        new_state = 'L'
                        changed = True
                    else:
                        new_state = self.seats[row][col]
                    new_row += new_state
                new_seats.append(new_row)
            self.seats = new_seats
            new_seats = []

    def occupied_visible(self, y, x):
        occupied = 0
        if x < self.width - 1:  # ->
            for dx in range(x + 1, self.width):
                if self.seats[y][dx] == '#':
                    occupied += 1
                    break
                if self.seats[y][dx] == 'L':
                    break
        if x > 0:  # <-
            for dx in range(x - 1, -1, -1):
                if self.seats[y][dx] == '#':
                    occupied += 1
                    break
                if self.seats[y][dx] == 'L':
                    break
        if y < self.height - 1:  # v
            for dy in range(y + 1, self.height):
                if self.seats[dy][x] == '#':
                    occupied += 1
                    break
                if self.seats[dy][x] == 'L':
                    break
        if y > 0:  # ^
            for dy in range(y - 1, -1, -1):
                if self.seats[dy][x] == '#':
                    occupied += 1
                    break
                if self.seats[dy][x] == 'L':
                    break
        if x < self.width - 1:
            if y < self.height - 1:  # -> v
                for dx, dy in zip(range(x + 1, self.width), range(y + 1, self.height)):
                    if self.seats[dy][dx] == '#':
                        occupied += 1
                        break
                    if self.seats[dy][dx] == 'L':
                        break
            if y > 0:  # -> ^
                for dx, dy in zip(range(x + 1, self.width), range(y - 1, -1, -1)):
                    if self.seats[dy][dx] == '#':
                        occupied += 1
                        break
                    if self.seats[dy][dx] == 'L':
                        break
        if x > 0:  # <-
            if y < self.height - 1:  # <- v
                for dx, dy in zip(range(x - 1, -1, -1), range(y + 1, self.height)):
                    if self.seats[dy][dx] == '#':
                        occupied += 1
                        break
                    if self.seats[dy][dx] == 'L':
                        break
            if y > 0:  # <- ^
                for dx, dy in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
                    if self.seats[dy][dx] == '#':
                        occupied += 1
                        break
                    if self.seats[dy][dx] == 'L':
                        break
        return occupied


s = Seats("inputs/11.in")
s.simulate_near()
print(s.occupied())

s = Seats("inputs/11.in")
s.simulate_visible()
print(s.occupied())
