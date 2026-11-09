# Q3: In Java, int[] arr = {1, "two", 3}; fails to compile. In Python, mixed = [1, "two", 3] works fine. Why?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# Python arrays silently convert every element to a string
#
# Python lists are heterogeneous -- they don't require every element to share one type, unlike Java/C++ arrays
# Correct answer
# Your answer
#
# C
# Python secretly stores every element as the same hidden type
#
# D
# Java arrays are actually more flexible than Python lists
# Explanation
#
# Python lists can freely mix types in one list (heterogeneous); Java/C++ arrays require every element to share the same declared type (homogeneous).
#
