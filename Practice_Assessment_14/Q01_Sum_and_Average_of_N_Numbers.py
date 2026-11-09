# Q1: Sum and Average of N Numbers

n = int(input())

if n == 0:
    print("Sum: 0")
    print("Average: 0.00")
else:
    nums = list(map(int, input().split()))
    total = sum(nums)

    print(f"Sum: {total}")
    print(f"Average: {total / n:.2f}")
