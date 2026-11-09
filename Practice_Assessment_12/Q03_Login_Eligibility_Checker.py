# Q3: Login Eligibility Checker

# Write your reference solution here
# Write your reference solution here
age , has_id,is_banned = map(int,input().split())
if age >= 18 and has_id == 1 and is_banned == 0 :
        print("Allowed")
else:
        print("Denied")
