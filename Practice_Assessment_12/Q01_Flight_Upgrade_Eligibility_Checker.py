# Q1: Flight Upgrade Eligibility Checker

member, miles = map(int, input().split())

if member == 1:
    if miles >= 100000:
        print("Eligible: Platinum Upgrade")
    elif miles >= 50000:
        print("Eligible: Gold Upgrade")
    else:
        print("Not Eligible: Insufficient Miles")
else:
    if miles >= 100000:
        print("Eligible: Standard Upgrade Offer")
    else:
        print("Not Eligible: Join Membership Program")
