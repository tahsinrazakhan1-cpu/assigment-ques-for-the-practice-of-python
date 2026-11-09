# Q4: An article-tagging system stores each article's tags as a set inside a list: article_tags = [{"Python","AI"}, {"Python","Web"}]. Why is a set the right choice for each article's tags, rather than a list of tags?

# This is a non-code question; the original question and answer details are preserved below.
#
#
# A
# Sets preserve the order tags were added in, which matters for display
#
# A set automatically prevents the same tag being added twice, and makes "does this article have tag X?" fast to check
# Correct answer
# Your answer
#
# C
# Sets take less memory than lists no matter what they store
#
# D
# Lists cannot hold strings, only sets can
# Explanation
#
# Tags naturally shouldn't repeat, and membership checks ("does this article have tag X?") are common -- exactly what sets are built for.
#
