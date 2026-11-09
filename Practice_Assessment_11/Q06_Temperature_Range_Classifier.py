# Q6: Temperature Range Classifier

# Write your reference solution here
x = int(input())
if   x<0 :
    print("Freezing")
elif   0<=x<15 : 
    print("Cold")
elif 15 <=x<25 :
    print("Mild")
elif 25 <=x<35:
    print("Hot")
else:
    print("Extreme Heat")
