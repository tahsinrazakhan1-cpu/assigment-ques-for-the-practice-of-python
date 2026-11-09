# Q11: A system needs to track which of 5 million user IDs have already redeemed a coupon, only ever asking "has this ID redeemed yet?". Which container fits best?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# list, because it preserves the order IDs redeemed in
#
# set, because only membership matters and lookups need to be fast
# Correct answer
# Your answer
#
# C
# str, because IDs are just text
#
# D
# tuple, because IDs never change
# Explanation
#
# Order doesn't matter here -- only fast membership checks do -- which is exactly what a set is optimized for.
#
