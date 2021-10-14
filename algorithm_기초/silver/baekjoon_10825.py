import sys

n = int(sys.stdin.readline())
student = []
for i in range(n):
    student.append(list(sys.stdin.readline().split()))

student = sorted(student, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in student:
    print(i[0])
