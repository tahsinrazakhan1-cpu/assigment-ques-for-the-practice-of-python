# Q2: Palindrome Checker II



x = str(input())
x = x.replace(" ","").lower()
if x == x[::-1] :
    print("Palindrome")
else :
    print('Not Palindrome')
