file = open("inputs/13.in")
time = int(file.readline())
lines = [line for line in file.readline().split(',')]
int_lines = [int(line) for line in lines if line != 'x']
nearest_departures = [(time // line + 1) * line for line in int_lines]
the_nearest = min(nearest_departures)
print((the_nearest - time) * int_lines[nearest_departures.index(the_nearest)])

result = 0
add = int(lines[0])
for i in range(1, len(lines)):
    if lines[i] != 'x':
        while (result % int(lines[0]) != 0) or ((result + i) % int(lines[i]) != 0):
            result += add
        add *= int(lines[i])
print(result)
