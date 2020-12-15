def last_number(starting, last_turn):
    numbers = {n: i + 1 for i, n in enumerate(starting)}
    last_spoken = 0
    for turn in range(len(starting) + 1, last_turn):
        if last_spoken in numbers.keys():
            old_last_spoken = last_spoken
            last_spoken = turn - numbers[last_spoken]
            numbers[old_last_spoken] = turn
        else:
            numbers[last_spoken] = turn
            last_spoken = 0
    return last_spoken


print(last_number([16, 12, 1, 0, 15, 7, 11], 2020))
print(last_number([16, 12, 1, 0, 15, 7, 11], 30000000))
