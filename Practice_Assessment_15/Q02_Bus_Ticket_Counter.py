# Q2: Bus Ticket Counter

# Write your reference solution here
pessanger = list(map(int , input().split()))
i =1
freeP= 0 
totalf = 0

while i < len(pessanger):
    if  pessanger[i] <=4 :
        freeP += 1 
    elif pessanger[i] <= 12 :
        totalf += 10
    elif pessanger[i] <=  59 :
        totalf += 25
    elif pessanger[i] <= 79 :
        totalf += 15
    else :
        freeP += 1
    i+=1

print(f"Total fare: {totalf}, Free passengers: {freeP}")
