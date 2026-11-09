# Q2: Coordinate Deduplicator

# Write your reference solution here
n = int(input())
unique_cordi = set()
for _ in range(n):
    x,y = map(int , input().split())
    unique_cordi.add((x,y))

print(len(unique_cordi))
for x in sorted(unique_cordi):
    print(*x,sep = " ")
