# Q5: Power-of-Two Checker

# Write your reference solution here
n =int(input())
if n>0 and ( n &(n-1))==0 :
    print("Yes")
else:
    print("No")
