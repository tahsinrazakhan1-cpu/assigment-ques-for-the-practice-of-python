# Q5: ATM Session

balance = int(input())

declined = 0
blocked = False

while True:
    transaction = int(input())

    if transaction == 0:
        break

    if transaction > 0:
        balance = balance + transaction

    else:
        amount = -transaction

        if balance >= amount:
            balance = balance - amount
        else:
            declined = declined + 1

            if declined == 3:
                blocked = True
                break

print(f"Final balance: {balance}")
print(f"Declined withdrawals: {declined}")

if blocked:
    print("Card blocked")
else:
    print("Session closed")
