def to_seat_id(chars):
    col_l = 0
    col_r = 8
    row_l = 0
    row_r = 128
    for c in chars:
        if c == 'F':
            row_r -= (row_r - row_l) // 2
        if c == 'B':
            row_l += (row_r - row_l) // 2
        if c == 'R':
            col_l += (col_r - col_l) // 2
        if c == 'L':
            col_r -= (col_r - col_l) // 2
    return col_l + row_l * 8


file = open("5.in")

ids = [to_seat_id(line) for line in file]
print(max(ids))

sorted_ids = sorted(ids)

for i in range(len(sorted_ids)):
    if not (i + sorted_ids[0]) == sorted_ids[i]:
        print(i + sorted_ids[0])
        break
