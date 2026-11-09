# Q1: Pascal's Triangle

# Write your reference solution here
import math 
n = int(input())
i = 0

while i < n :
        j = 0
        while j <= i :
                cobi = round(math.factorial(i)/(math.factorial(j)*math.factorial(i -j)))
                if i == j :
                        print(cobi)
                else :
                        print(cobi, end = " ")
                j += 1
        # print()
        i += 1
