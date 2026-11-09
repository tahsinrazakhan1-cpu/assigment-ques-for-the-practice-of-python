# Q1: Reversed Copy, Different Box

original = input()

reversed_copy = original[::-1]

print(f"Length: {len(original)}")
print(f"Reversed: {reversed_copy}")
print(f"Same object as original: {id(original) == id(reversed_copy)}")
