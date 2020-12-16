import re
from functools import reduce


class Field:
    field_re = re.compile("([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)")

    def __init__(self, line):
        groups = self.field_re.match(line).groups()
        self.name = groups[0]
        self.lower_from = int(groups[1])
        self.lower_to = int(groups[2])
        self.upper_from = int(groups[3])
        self.upper_to = int(groups[4])

    def invalid_fields(self, ticket):
        invalid = []
        for field in ticket:
            if not self.valid_field(field):
                invalid.append(field)
        return invalid

    def valid_field(self, value):
        return self.lower_from <= value <= self.lower_to or self.upper_from <= value <= self.upper_to

    def __repr__(self):
        return f"{self.name}: {self.lower_from}-{self.lower_to} or {self.upper_from}-{self.upper_to}"


file = open("inputs/16.in")
fields = []

for line in file:
    if line == '\n':
        break
    fields.append(Field(line))

file.readline()
my_ticket = [int(n) for n in file.readline().split(',')]

file.readline()
file.readline()
nearby_tickets = []
for line in file:
    nearby_tickets.append([int(n) for n in line.split(',')])

sum_of_invalid = 0
valid_tickets = []
for ticket in nearby_tickets:
    fields_to_check = ticket
    for field in fields:
        fields_to_check = field.invalid_fields(fields_to_check)
    sum_of_invalid += sum(fields_to_check)
    if len(fields_to_check) == 0:
        valid_tickets.append(ticket)
print(sum_of_invalid)

possible_fields = []
for i in range(len(my_ticket)):
    possible_fields.append(set(range(len(fields))))

for ticket in valid_tickets:
    for tn, value in enumerate(ticket):
        for fn, field in enumerate(fields):
            if (not field.valid_field(value)) and fn in possible_fields[tn]:
                possible_fields[tn].remove(fn)


reduced_fields = [0] * len(possible_fields)
for _ in possible_fields:
    number_to_reduce = 0
    for i, p in enumerate(possible_fields):
        if len(p) == 1:
            number_to_reduce = p.pop()
            reduced_fields[i] = number_to_reduce
            break
    for i, p in enumerate(possible_fields):
        if number_to_reduce in p:
            p.remove(number_to_reduce)

values = (my_ticket[index] for index, field in enumerate(reduced_fields) if fields[field].name.startswith("departure"))
product_of_departures = reduce(lambda x, y: x*y, values)
print(product_of_departures)
