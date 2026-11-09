# Q2: Add Two Matrices

# # Write your reference solution here
# R,C = map(int,input().split())
# n = 2
# p = 0 
# mat1= []
# i = 0
# while i < R:
#     mithu = list(map(int,input().split()))
#     mat1.append(mithu)
#     i += 1 
# mat2 = []
# i = 0
# while i < R :
#     mithu = list(map(int,input().split()))
#     mat2.append(mithu)
#     i += 1
# # succesfully take two list 
# sum_matrix = []

# i = 0 
# while i < R :
#     j = 0 
#     meow = []
#     while j < C :
#         nene = mat1[i][j] + mat2[i][j]
#         meow.append(nene)
#         j += 1 
#     sum_matrix.append(meow)
#     i += 1             

# # print(sum_matrix)
# # succesfully make the sum matrix now have to print 
# i = 0 
# while i < R :
#     print(*sum_matrix[i])
#     i += 1 

 
# more good solutions 

R,C = map(int,input().split())
mat1 = []
for i in range(R):
    mat1.append(list(map(int,input().split())))
mat2 = []
for i in range(R):
    mat2.append(list(map(int,input().split())))
# print(mat1)
# print(mat2)
for i in range(R):
    for j in range(C):
        if j == C - 1 :
            print(mat1[i][j] + mat2[i][j]) 
        else :
            print(mat1[i][j] + mat2[i][j],end = " ")
