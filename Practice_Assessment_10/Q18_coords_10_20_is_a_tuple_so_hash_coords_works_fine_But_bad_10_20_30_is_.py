# Q18: coords = (10, 20) is a tuple, so hash(coords) works fine. But bad = (10, [20, 30]) is also a tuple. What happens when you run hash(bad)?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# Works fine -- tuples are always hashable
#
# TypeError: unhashable type: 'list', because one of the tuple's elements is a mutable list
# Correct answer
# Your answer
#
# C
# Returns 0, since the tuple contains a nested container
#
# D
# Works, but returns a different hash value every time the program runs
# Explanation
#
# A tuple is only hashable if every element inside it is also hashable. Nesting a mutable list inside an otherwise-immutable tuple breaks that guarantee.
#
