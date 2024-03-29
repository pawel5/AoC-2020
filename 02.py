import re

expression = re.compile("(\d+)-(\d+) ([a-z]): (\w+)")


counter = 0
file = open("inputs/02.in")
for line in file:
    (f, to, c, password) = expression.findall(line)[0]
    if int(f) <= password.count(c) <= int(to):
        counter += 1
print(counter)

counter = 0

file.seek(0)
for line in file:
    (f, to, c, password) = expression.findall(line)[0]
    f = int(f)
    to = int(to)
    if (password[f-1] == c and password[to-1] != c) or (password[f-1] != c and password[to-1] == c):
        counter += 1
print(counter)
