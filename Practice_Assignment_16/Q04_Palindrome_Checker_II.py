# Q4: Palindrome Checker II

# Write your reference solution here


x = str(input())
x = x.replace(" ","").lower()
if x == x[::-1] :
    print("Palindrome")
else :
    print('Not Palindrome')
