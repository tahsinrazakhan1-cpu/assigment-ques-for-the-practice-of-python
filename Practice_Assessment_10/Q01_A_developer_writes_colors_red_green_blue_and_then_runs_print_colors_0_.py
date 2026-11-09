# Q1: A developer writes colors = {"red", "green", "blue"} and then runs print(colors[0]) expecting to see the first color. What actually happens?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# Prints "red"
#
# B
# Prints a random element from the set
#
# Raises TypeError: 'set' object is not subscriptable
# Correct answer
# Your answer
#
# D
# Raises IndexError: set index out of range
# Explanation
#
# Sets are unordered and don't track positions, so Python doesn't support indexing on them at all -- it raises TypeError rather than guessing an element.
#
