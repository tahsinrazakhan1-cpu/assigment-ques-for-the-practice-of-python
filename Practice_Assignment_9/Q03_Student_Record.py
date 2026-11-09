# Q3: Student Record

# Write your reference solution here
name, s1, s2, s3 = input().split()

student = (name, int(s1), int(s2), int(s3))

avg = (student[1] + student[2] + student[3]) / 3

print(f"{student[0]} {avg:.2f}")
