# Q13: A student runs: label = "Sale" then label[0] = "s". What happens?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# label becomes "sale"
#
# TypeError: 'str' object does not support item assignment
# Correct answer
# Your answer
#
# C
# label becomes "Sale " with a trailing space
#
# D
# No error, but label is left unchanged
# Explanation
#
# Strings are immutable in Python -- their characters can never be changed in place after creation, so item assignment raises TypeError.
#
