# Q1: Matrix TotaL

# Write your reference solution here
R, C = map(int, input().split())
mat = [ ]
i = 0
while i < R :
        row = list(map(int,input().split()))
        mat.append(row)
        i += 1

sumu = 0
row = 0
while row < R:
    col = 0 
    while col < C :
        sumu += mat[row][col]
        col += 1
    row +=1 

print(sumu)
