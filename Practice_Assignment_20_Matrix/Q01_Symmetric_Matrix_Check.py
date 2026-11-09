# Q1: Symmetric Matrix Check

# # Write your reference solution here
n = int(input())
i = 0 
matriwa = []
while i < n :
    matu = list(map(int,input().split()))
    matriwa.append(matu)
    i += 1

# # print(matriwa) taking the list is complete 
# # task 2 
# i = 0 

# while i < n :
#     j = 0 
#     sym = False
#     while j < n :
#         if matriwa[i][j] == matriwa[j][i] :
#             sym = True
#         else :
#             sym = False
#             # print("Not Symmetric")
#             break
#         j += 1 
#     i += 1
# if sym:
#     print("Symmetric")
# else :
#     print("Not Symmetric")
        
# above code is done jesse tesse i want to make a more cleanner code how i able to do that 

# lets undertands the logic task one to check only important things lesss loops cycles lesss computing 
#2. trues false of sym clean 

# 2nd trial of the code 

# i = 0 
# sym = True
# while i < n :
#     j = 0 
#     while j < n :
#         if matriwa[i][j] != matriwa[j][i]:
#             sym = False
#             break
#         j += 1
#     if  not sym:
#         break
#     i+=1

# if sym :
#     print("Symmetric") 
# else :
#     print("Not Symmetric")

# it is lot more cleaner but there is more simple less computing way 
# less checks above the diagonals parts 

i = 0 
sym = True
while i < n :
    # change 
    j = i + 1 
    while j < n :
        if matriwa[i][j] != matriwa[j][i]:
            sym = False
            break
        j += 1
    if  not sym:
        break
    i+=1

if sym :
    print("Symmetric") 
else :
    print("Not Symmetric")
