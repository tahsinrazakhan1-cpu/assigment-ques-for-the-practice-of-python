# Q1: Triangle Type Classifier

# Write your reference solution here
S1,S2,S3 = map(int,input().split())
if S1 + S2 > S3 :
    if S1 ==S2==S3 :
        print("Equilateral")
    elif S1==S2 or S2==S3 or S1==S3 :
        print("Isosceles")
    else :
        print("Scalene")
else:
    print("Not a Triangle")
