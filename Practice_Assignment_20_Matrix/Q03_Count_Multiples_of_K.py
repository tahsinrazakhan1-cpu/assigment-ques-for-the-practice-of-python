# Q3: Count Multiples of K

# Write your reference solution here
R,C,K = map(int,input().split())
mat = []
for i in range(R):
        mat.append(list(map(int,input().split())))
# print(mat)
# print(K)
# succefully taken the list 


# here the main solutiomn
# count = 0
# for i in range(R):
#     for j in range(C):
#         if mat[i][j] % K == 0 :
#             count += 1 
# print(count) 



# there is even shorter way to do it 
count=0
for i in mat:
    for j in i:
        if j % K == 0 :
            count += 1 
print(count)
