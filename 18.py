file = open("inputs/18.in")
result = 0
for line in file:
    line = line[:-1].replace('(', "( ").replace(')', " )")
    splitted = line.split(' ')
    while len(splitted) > 1:
        for i, (l, op, r) in enumerate(zip(splitted, splitted[1:], splitted[2:])):
            if l == '(' and r == ')':
                splitted = splitted[:i] + [op] + splitted[i+3:]
                break
            if op == "+" and l != ')' and r != '(':
                splitted = splitted[:i] + [str(int(l) + int(r))] + splitted[i+3:]
                break
            if op == "*" and l != ')' and r != '(':
                splitted = splitted[:i] + [str(int(l) * int(r))] + splitted[i+3:]
                break
    result += int(splitted[0])
print(result)

file.seek(0)
result = 0
for line in file:
    line = line[:-1].replace('(', "( ").replace(')', " )")
    splitted = line.split(' ')
    while len(splitted) > 1:
        max_braces_level = 0
        braces_level = 0
        for c in splitted:
            if c == '(':
                braces_level += 1
                if braces_level > max_braces_level:
                    max_braces_level = braces_level
            if c == ')':
                braces_level -= 1
        try_multiplication = True
        for i, (l, op, r) in enumerate(zip(splitted, splitted[1:], splitted[2:])):
            if l == '(':
                braces_level += 1
            if r == ')':
                braces_level -= 1
            if l == '(' and r == ')':
                splitted = splitted[:i] + [op] + splitted[i+3:]
                try_multiplication = False
                break
            if op == "+" and l != ')' and r != '(' and braces_level == max_braces_level:
                splitted = splitted[:i] + [str(int(l) + int(r))] + splitted[i+3:]
                try_multiplication = False
                break
        if try_multiplication:
            for i, (l, op, r) in enumerate(zip(splitted, splitted[1:], splitted[2:])):
                if l == '(':
                    braces_level += 1
                if r == ')':
                    braces_level -= 1
                if op == "*" and l != ')' and r != '(' and braces_level == max_braces_level:
                    splitted = splitted[:i] + [str(int(l) * int(r))] + splitted[i+3:]
                    break
    result += int(splitted[0])
print(result)
