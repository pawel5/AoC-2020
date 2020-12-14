import re

regex = re.compile("[a-z]{3}:")
items = set()
file = open("inputs/04.in")
valid = 0
for line in file:
    for item in re.findall(regex, line):
        items.add(item)
    if line == "\n":
        if {'iyr:', 'byr:', 'pid:', 'hcl:', 'eyr:', 'ecl:', 'hgt:'}.issubset(items):
            valid += 1
        items.clear()
if {'iyr:', 'byr:', 'pid:', 'hcl:', 'eyr:', 'ecl:', 'hgt:'}.issubset(items):
    valid += 1
print(valid)

hgt_regexp = re.compile("^([0-9]+)(in|cm)$")
hcl_regexp = re.compile("^#[0-9a-f]{6}$")
ecl_regexp = re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$")
pid_regexp = re.compile("^[0-9]{9}$")


def check(items_set):
    byr = items_set.get("byr")
    if byr is None:
        return False
    if not 1920 <= int(byr) <= 2002:
        return False

    iyr = items_set.get("iyr")
    if iyr is None:
        return False
    if not 2020 >= int(iyr) >= 2010:
        return False

    eyr = items_set.get("eyr")
    if eyr is None:
        return False
    if not 2030 >= int(eyr) >= 2020:
        return False

    hgt = items_set.get("hgt")
    if hgt is None:
        return False
    matches = hgt_regexp.match(hgt)
    if matches is None:
        return False
    if matches.group(2) != "cm" and matches.group(2) != "in":
        return False
    if matches.group(2) == "cm" and not 150 <= int(matches.group(1)) <= 195:
        return False
    if matches.group(2) == "in" and not 59 <= int(matches.group(1)) <= 76:
        return False

    hcl = items_set.get("hcl")
    if hcl is None:
        return False
    if not hcl_regexp.match(hcl):
        return False

    ecl = items_set.get("ecl")
    if ecl is None:
        return False
    if not ecl_regexp.match(ecl):
        return False

    pid = items_set.get("pid")
    if pid is None:
        return False
    if not pid_regexp.match(pid):
        return False

    return True


regex = re.compile("([a-z]{3}):([#0-9a-z]+)")
items = {}
file.seek(0)
valid = 0
for line in file:
    for (key, value) in re.findall(regex, line):
        items[key] = value
    if line == "\n":
        if check(items):
            valid += 1
        items = {}
if check(items):
    valid += 1
print(valid)
