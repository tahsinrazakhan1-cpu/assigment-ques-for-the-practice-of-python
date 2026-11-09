# Q17: You need to check membership of an ID against 2 million stored IDs, many times per second. Which container gives the fastest average-case lookup?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# list
#
# B
# str
#
# set
# Correct answer
# Your answer
#
# D
# All three perform identically
# Explanation
#
# Sets use hashing internally, giving roughly O(1) average-case membership checks, while lists require scanning up to every element -- O(n).
#
