# Q3: Binary Triangle

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= i:
        if (i + j) % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
            
        if j < i:
            print(" ", end="")
        j += 1

    print()
    i += 1
