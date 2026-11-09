# Q2: Traffic Signal Action

# Write your reference solution here
a = str(input())
if  a in ["red","yellow","green"]:
    if a =="red":
        print("Stop")
    elif a=="green":
        print("Go")
    elif a=="yellow":
        print("Slow Down")
else :
    print("Unknown Signal")
