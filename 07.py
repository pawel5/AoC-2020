import re

rule_regexp = re.compile("(?P<count>[0-9]*) ?(?P<color>[a-z]+ [a-z]+) bags?")


def rule_to_entry(rule):
    match = rule_regexp.findall(rule)
    root = match.pop(0)[1]
    colors = []
    for leaf in match:
        colors.append((leaf[0], leaf[1]))
    return root, colors


def file_to_rules(file_name):
    file = open(file_name)
    file_rules = {}
    for line in file:
        (key, values) = rule_to_entry(line)
        file_rules[key] = values
    return file_rules


def find_keys_for(entry, rules):
    keys = set()
    for key, values in rules.items():
        for value in values:
            if value[1] == entry:
                keys.add(key)
    if len(keys) > 0:
        keys_to_iterate = keys.copy()
        for key in keys_to_iterate:
            keys.update(find_keys_for(key, rules))
    return keys


rules = file_to_rules("inputs/07.in")
print(len(find_keys_for("shiny gold", rules)))


def count_bags_for(key, rules):
    counter = 0
    for rule in rules[key]:
        if not rule[1] == "no other":
            number_of_bags = int(rule[0])
            counter += number_of_bags + number_of_bags * count_bags_for(rule[1], rules)
    return counter


rules = file_to_rules("inputs/07.in")
print(count_bags_for("shiny gold", rules))
