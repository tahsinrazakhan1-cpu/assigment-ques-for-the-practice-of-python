# Q15: A junior developer says: "Lists and sets both let me loop through elements, so they're basically the same for storing data." What key idea about "ordered" are they missing?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# Ordered containers store items alphabetically; unordered containers don't
#
# Ordered containers remember each item's position, so element[i] is meaningful; unordered containers only track membership, not position
# Correct answer
# Your answer
#
# C
# Ordered containers are always faster to search than unordered containers
#
# D
# There is no real difference -- both preserve insertion order in modern Python
# Explanation
#
# Ordered means Python keeps track of each element's position, so you can ask 'what's at position 2?'. Unordered means Python only tracks whether an item is present, not where.
#
