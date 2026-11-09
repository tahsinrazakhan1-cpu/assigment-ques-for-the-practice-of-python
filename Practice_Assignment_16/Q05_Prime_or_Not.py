# Q5: Prime or Not


num = int(input())
i = 1
count = 0
while i <=  num:
    if num %i == 0:
        count +=1
    i+=1
if count == 2:
    print("prime")
else :
    print("not prime")
