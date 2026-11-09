# Q4: Diagonal Sums

# Write your reference solution here
# Write your reference solution here
R = int(input())
mat = []
i = 0 
while i < R :
        l = list(map(int,input().split()))
        mat.append(l)
        i+=1

# print(mat)

sum_main = 0
sum_anti = 0

i = 0
while i < R :
        sum_main += mat[i][i]
        i+= 1 
# print(sum_main)

row = 0
coll = (R-1)
while row < R:
        sum_anti += mat[row][coll]
        row += 1
        coll -= 1

print(sum_main,sum_anti)
