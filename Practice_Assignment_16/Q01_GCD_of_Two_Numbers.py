# Q1: GCD of Two Numbers

# Write your reference solution here
a,b = map(int , input().split())
while b != 0 :
    r = a % b
    a = b
    b= r
print(a)
