# Q4: Longest Word in a Sentence

x = input().split()
i=0
ster1 = ""
c=0

while i < len(x):
    if len(x[i])>c :
        c=len(x[i])
        ster1 = x[i]
    i += 1
        
print(ster1)
