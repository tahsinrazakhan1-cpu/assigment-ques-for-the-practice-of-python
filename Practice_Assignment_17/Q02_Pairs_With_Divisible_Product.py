# Q2: Pairs With Divisible Product

# Write your reference solution here
n , k = map(int, input().split())
count = 0 
i  = 1

while i <= n :
    j = i + 1
    while j <= n :
        product = i * j 
        if product % k == 0 :
            count += 1 
        j+= 1 
    i+=1 
print(count)
