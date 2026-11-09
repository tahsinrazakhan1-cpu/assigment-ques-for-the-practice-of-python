# Q8: A leaderboard stores the top 10 scores in ranked order, and rank #3 sometimes needs correcting after a review. Which container fits best?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# set, because scores shouldn't repeat
#
# list, because order matters and an element needs to be updated by position
# Correct answer
# Your answer
#
# C
# str, because scores can just be joined as text
#
# D
# Doesn't matter, all three behave the same way here
# Explanation
#
# This needs both order (ranking) and mutation by position (correcting rank #3) -- exactly what a list provides.
#
