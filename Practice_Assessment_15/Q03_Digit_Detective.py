# Q3: Digit Detective

# Write your reference solution here
n = int(input())
zero = 0
even = 0
odd = 0
if n == 0:
    zero = 1 

while n > 0 :
    digit = n%10 
    if digit == 0 :
        zero += 1 
    elif n% 2 == 0 :
        even += 1 
    else :
         odd += 1 
    n = n//10
print(f"Even: {even}, Odd: {odd}, Zero: {zero}")
