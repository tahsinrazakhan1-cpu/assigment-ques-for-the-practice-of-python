# Q2: Row Sums and Column Sums

R, C = map(int, input().split())

mat = []

i = 0
while i < R:
    row = list(map(int, input().split()))
    mat.append(row)
    i += 1

sun_r = []  # row sums
sun_c = []  # column sums

# Find row sums
row = 0
while row < R:
    col = 0
    total = 0

    while col < C:
        total += mat[row][col]
        col += 1

    sun_r.append(total)
    row += 1

# Find column sums
col = 0
while col < C:
    row = 0
    total = 0

    while row < R:
        total += mat[row][col]
        row += 1

    sun_c.append(total)
    col += 1

print(*sun_r)
print(*sun_c)
