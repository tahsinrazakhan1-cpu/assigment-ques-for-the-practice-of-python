# Q5: A list data = [10, "20", 30] is meant to store three numbers for a total, but one value is accidentally a string. What happens when the program later runs sum(data)?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# Python auto-converts "20" to the number 20
#
# TypeError, because Python won't silently add an int and a str together
# Correct answer
# Your answer
#
# C
# The string is skipped and sum() ignores it
#
# D
# sum() returns "102030" as one concatenated string
# Explanation
#
# Python's flexibility in mixing types in a list is powerful but risky -- an operation like sum() will crash with a TypeError the moment it hits an incompatible type.
#
