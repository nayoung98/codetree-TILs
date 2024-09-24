import sys

input = sys.stdin.readline
n = int(input())

class StudentInfo:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

student_list = []
for i in range(n):
    height, weight = map(int, input().split())
    student_info = StudentInfo(height, weight, i+1)

    student_list.append(student_info)

student_list.sort(key=lambda x: (x.height, -x.weight)) 

for student in student_list:
    print(student.height, student.weight, student.number)