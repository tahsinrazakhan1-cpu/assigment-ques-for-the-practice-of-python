# Q1: Max Number Grid

n = int(input())

i = 1
while i <= n :
    j = 1 
    while j <= n :
        if j ==n :
            print(max(i,j))
        else:
            print(max(i,j), end = " ")
        j+=1
    i+=1
