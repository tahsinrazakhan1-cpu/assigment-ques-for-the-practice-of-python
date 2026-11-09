# Q12: A robot's visited grid positions are stored as visited = {(0,0), (1,1), (0,0), (2,3)}. What is len(visited), and why does this work when a set of lists wouldn't?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# len is 4; tuples and lists both work fine as set elements
#
# len is 3; tuples are hashable (immutable), so they can be set elements, unlike lists
# Correct answer
#
# len is 4; sets never deduplicate tuples
# Your answer
#
# D
# This raises a TypeError, since tuples can't be compared for equality
# Explanation
#
# (0,0) is repeated and gets deduplicated, leaving 3 unique tuples. Tuples are immutable and therefore hashable, so they're valid set elements -- lists are not.
#
