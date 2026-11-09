# Q3: Multiplication Table Grid

# Write your reference solution here
R,C = map(int , input().split())
i = 1
while i <= R :
        j = 1
        while j <= C :
                if j < C :
                        print(i*j , end= " ")
                elif j == C :
                        print(i*j , end= "")

                j += 1 
        i += 1 
        print()
