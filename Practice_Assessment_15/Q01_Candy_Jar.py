# Q1: Candy Jar

candies = int(input())

k = 1
children = 0

while candies > 0:
    children += 1

    if candies >= k:
        last_got = k
        candies = candies - k

        if candies == 0:
            full_share = "Yes"

    else:
        last_got = candies
        candies = 0
        full_share = "No"

    k += 1

print(f"Children: {children}, Last child got: {last_got}, Full share: {full_share}")
