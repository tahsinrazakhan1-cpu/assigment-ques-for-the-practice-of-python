# Q3: Transpose of Matrix

# Write your reference solution here
# Write your reference solution here
R, C = map(int, input().split())
mat = [ ]
i = 0
while i < R :
        row = list(map(int,input().split()))
        mat.append(row)
        i += 1

col = 0 
while col < C :
        row = 0 
        while row < R :
                if row == R -1 :
                        print(mat[row][col])
                else:
                        print(mat[row][col] , end = " ")
                row += 1 
        
        col += 1
