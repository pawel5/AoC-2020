from collections import Counter

jolts = sorted(int(jolt) for jolt in open("inputs/10.in"))
laptop = [jolts[-1] + 3]
all_jolts = [0] + jolts + laptop
differences = Counter(map(lambda pair: pair[1] - pair[0], zip(all_jolts[0:-1], all_jolts[1:])))
print(differences[1] * differences[3])


def series_element(nth):
    start = [1, 2, 4]
    if nth <= len(start):
        return start[nth-1]
    else:
        for i in range(3, nth):
            start.append(start[-1] + start[-2] + start[-3])
        return start[nth-1]


series = 0
combinations = 1
for jolt_diff in map(lambda pair: pair[1] - pair[0], zip(all_jolts[0:-1], all_jolts[1:])):
    if jolt_diff == 1:
        series += 1
    elif series > 0:
        combinations *= series_element(series)
        series = 0
print(combinations)
