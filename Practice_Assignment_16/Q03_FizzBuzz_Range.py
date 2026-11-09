# Q3: FizzBuzz Range


# Write your reference solution here
a , b = map(int, input().split())
i= a
while   i  <= b :
        if i%3 ==0 and i%5==0 :
                print("FizzBuzz")
        elif i%3 ==0 :
                print("Fizz")
        elif i%5==0:
                print("Buzz")
        else :
                print(i)
        i += 1
