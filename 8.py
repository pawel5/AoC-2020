class Nop:
    def __init__(self, value):
        self.value = value

    def exec(self, acc, curr_instr_ptr):
        return acc, curr_instr_ptr + 1


class Acc:
    def __init__(self, value):
        self.value = value

    def exec(self, acc, curr_instr_ptr):
        return acc + self.value, curr_instr_ptr + 1


class Jmp:
    def __init__(self, value):
        self.value = value

    def exec(self, acc, curr_instr_ptr):
        return acc, curr_instr_ptr + self.value


def check_execution(instructions):
    acc = 0
    instr_ptr = 0
    executed = set()

    while instr_ptr not in executed and instr_ptr < len(instructions):
        executed.add(instr_ptr)
        acc, instr_ptr = instructions[instr_ptr].exec(acc, instr_ptr)
    return instr_ptr == len(instructions), acc


instructions = []
file = open("8.in")
for line in file:
    instr, val = line.split(" ")
    if instr == "nop":
        instructions.append(Nop(int(val)))
    if instr == "acc":
        instructions.append(Acc(int(val)))
    if instr == "jmp":
        instructions.append(Jmp(int(val)))

result, acc = check_execution(instructions)

print(acc)

for index, instr in enumerate(instructions):
    if type(instr) is Nop:
        instructions[index] = Jmp(instr.value)
        result, acc = check_execution(instructions)
        if result:
            print(acc)
            break
        else:
            instructions[index] = instr
    if type(instr) is Jmp:
        instructions[index] = Nop(instr.value)
        result, acc = check_execution(instructions)
        if result:
            print(acc)
            break
        else:
            instructions[index] = instr
