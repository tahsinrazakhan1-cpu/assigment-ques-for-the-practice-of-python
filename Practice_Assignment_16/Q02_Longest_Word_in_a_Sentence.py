# Q2: Longest Word in a Sentence

# Write your reference solution here
a = input().split()
i = 1
max_word = a[0]
while i < len(a):
    if len(a[i]) > len(max_word) :
        max_word = a[i]
    i += 1
print(max_word)
