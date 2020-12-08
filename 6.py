file = open("inputs/6.in")

answers_sum = 0
group = set()
for line in file:
    if line == "\n":
        answers_sum += len(group)
        group = set()
    else:
        for c in line:
            if not c == '\n':
                group.add(c)
answers_sum += len(group)

print(answers_sum)

file.seek(0)

groups = []
same_answers_sum = 0
group = set()
for line in file:
    if line == "\n":
        answers_intersect = groups.pop(0)
        for g in groups:
            answers_intersect = answers_intersect.intersection(g)
        same_answers_sum += len(answers_intersect)
        groups.clear()
    else:
        group = set()
        for c in line:
            if not c == '\n':
                group.add(c)
        groups.append(group)

answers_intersect = groups.pop(0)
for g in groups:
    answers_intersect = answers_intersect.intersection(g)
same_answers_sum += len(answers_intersect)

print(same_answers_sum)
