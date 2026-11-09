# Q19: Which of these add() calls on s = {1, 2, 3} will crash with a TypeError?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# s.add(100)
#
# B
# s.add("hello")
#
# s.add((4, 5))
# Your answer
#
# s.add([4, 5])
# Correct answer
# Explanation
#
# Lists are mutable, and mutable built-in types are not hashable -- sets require every element to be hashable, so adding a list crashes.
#
