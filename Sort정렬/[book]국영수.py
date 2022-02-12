n = int(input())
student = []
for _ in range(n):
    student.append(input().split())
# [0]:이름 [1]:국 [2]:영 [3]:수
student.sort(
    key=lambda student: (-int(student[1]), int(student[2]), -int(student[3]), student[0]))

for name in student:
    print(name[0])
