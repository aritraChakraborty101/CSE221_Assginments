# Task 3:
# Suppose you are given a task to rank the students. You have gotten the marks and id of
# the students. Now your task is to rank the students based on their marks using a sorting
# algorithm.
# However, you have to keep in mind that your sorting algorithms perform the
# minimum number of swapping operations.
#
# Input:
# The first line of the input file will contain an integer N ( 1 ≤ N ≤ 1000 ).
# The second line will contain N integers, representing the Student ID, Si ( 1 ≤ Si ≤ 1000 ).
# The next line will contain the N integer, Sm ( 1 ≤ Sm ≤ 1000 ), which denotes the
# obtained mark of the corresponding students.
# Output:
# You have to show the Student Id and obtained marks in descending order based on
# their obtained mark. If two or more students get the same mark, then students with the
# lower ID will get prioritized. See the input and output for a better understanding.
# Input 1:
# 7
# 7 4 9 3 2 5 1
# 40 50 50 20 10 10 10
#
# Output 1:
# ID: 4 Mark: 50
# ID: 9 Mark: 50
# ID: 7 Mark: 40
# ID: 3 Mark: 20
# ID: 1 Mark: 10
# ID: 2 Mark: 10
# ID: 5 Mark: 10
#
# Input 2:
# 4
# 7 2 5 3
# 80 60 80 50
#
# Output 2:
# ID: 5 Mark: 80
# ID: 7 Mark: 80
# ID: 2 Mark: 60
# ID: 3 Mark: 50
#
# Please note, you have to take the input from an input3.txt file, and show the
# output in an output3.txt file



inp = open("E:\LabSection01_22101892_CSE221LabAssignment1_Summer2023\input3.txt","r")
out = open("E:\LabSection01_22101892_CSE221LabAssignment1_Summer2023\output3.txt", "w")

n = int(inp.readline())
id = []
mark = []

line = inp.readline().split(" ")
for i in range(len(line)):
    id.append(int(line[i]))

line2 = inp.readline().split(" ")
for i in range(len(line2)):
    mark.append(int(line2[i]))

for i in range(n):
    flag = False
    for j in range(0, n - 1):
        if mark[j] < mark[j + 1]:
            temp = mark[j]
            mark[j] = mark[j + 1]
            mark[j + 1] = temp
            id[j], id[j + 1] = id[j + 1], id[j]
            flag = True
        elif mark[j] == mark[j + 1]:
            if id[j] > id[j + 1]:
                curr = id[j]
                id[j] = id[j + 1]
                id[j + 1] = curr
                mark[j], mark[j + 1] = mark[j + 1], mark[j]
                flag = True

    if not flag:
        break

for i in range(n):
    out.writelines(f"ID: {id[i]} Mark: {mark[i]}\n")