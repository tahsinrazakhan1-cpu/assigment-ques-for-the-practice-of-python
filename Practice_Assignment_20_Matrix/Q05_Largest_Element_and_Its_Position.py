# Q5: Largest Element and Its Position

# Write your reference solution here
R,C = map(int,input().split())
mat = []
    
for i in range(R):
        mat.append(list(map(int,input().split())))
# succefully taken the matrix
largest_element = mat[0][0]
cordi_i = 1
cordi_j = 1
for i in range(R):
    for j in range(C):
        if mat[i][j] > largest_element :
            largest_element = mat[i][j]
            cordi_i = i+1
            cordi_j = j+1

print(largest_element,cordi_i,cordi_j)
