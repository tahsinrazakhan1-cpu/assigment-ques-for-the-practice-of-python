# Q2: Checkerboard

R, C = map(int, input().split())

i = 0
while i < R:
    j = 0
    while j < C:
        if (i + j) % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
        j += 1
    print()
    i += 1
