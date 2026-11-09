# Q4: Magic Number Shrinker

# Write your reference solution here
n = int(input())
steps = 0 

while n >= 10 :
    old = n 
    digit_sum = 0 
    while n > 0 : 
        digit = n%10 
        digit_sum = digit_sum + digit
        n = n//10

    print(f"{old} -> {digit_sum}")
    n = digit_sum
    steps += 1

print(f"Single digit: {n}")
print(f"Steps: {steps}")
