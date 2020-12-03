import functools
import operator


count = [0, 0, 0, 0, 0]
index = [0, 0, 0, 0, 0]
step_right = [1, 3, 5, 7, 1]
step_down = [1, 1, 1, 1, 2]
line_num = 0
file = open("input")

for line in file:
    for i in range(len(index)):
        if line_num % step_down[i] == 0:
            if line[index[i]] == "#":
                count[i] += 1
            index[i] = (index[i] + step_right[i]) % (len(line)-1)
    line_num += 1
print(count[1])
print(functools.reduce(operator.mul, count))
