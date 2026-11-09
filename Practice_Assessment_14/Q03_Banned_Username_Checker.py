# Q3: Banned Username Checker

n = int(input())

banned = set(input().split())

q = int(input())

users = input().split()

for user in users:
    if user in banned:
        print("BANNED")
    else:
        print("OK")
