# Q4: Sum of Border Elements

# Write your reference solution here
R,C = map(int,input().split())
mat = []
    
for i in range(R):
        mat.append(list(map(int,input().split())))
# print(mat)
# list is taken 
sumOFAll= 0
if R == 1 or C == 1 :
    for i in range(R):
        for j in range(C):
            sumOFAll += mat[i][j]
else :
    for i in range(R):
        if i == 0 or i == R - 1 :
            for j in range(C):
                sumOFAll += mat[i][j]
        else :
            sumOFAll += mat[i][0]
            sumOFAll += mat[i][C-1]
print(sumOFAll)
