f = open("input")
lines = [int(line) for line in f]
for i in range(len(lines)):
    for j in range(i, len(lines)):
        if lines[i] + lines[j] == 2020:
            print(f"Two numbers: {lines[i]} * {lines[j]} = {lines[i] * lines[j]}")
        for k in range(j, len(lines)):
            if lines[i] + lines[j] + lines[k] == 2020:
                print(f"Three numbers: {lines[i]} * {lines[j]} * {lines[k]} = {lines[i] * lines[j] * lines[k]}")