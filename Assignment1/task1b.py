# b) You are given a file “input1b.txt”. The first line of the input file will contain an integer T,
# representing the number of test cases. The next T lines will contain a single arithmetic
# expression. Each arithmetic expression will start with the prefix “calculate“. It is
# guaranteed that the expression will have exactly two operands and one operator.
# Calculate the result of each expression. Your output format should exactly match with
# the sample output format. All the results must be compiled in a single file,
# “output1b.txt.”
# Sample Input File Sample Output File
# 15
# calculate 67 + 41
# calculate 85 / 5
# calculate 13 - 56
# calculate 99 - 95
# calculate 3 / 10
# calculate 12 * 19
# calculate 14 - 6
# calculate 3 * 88
# calculate 45 * 68
# calculate 81 - 0
# calculate 77 + 40
# calculate 8 * 84
# calculate 73 - 22
# calculate 85 - 86
# calculate 28 * 58
#
# The result of 67 + 41 is 108
# The result of 85 / 5 is 17.0
# The result of 13 - 56 is -43
# The result of 99 - 95 is 4
# The result of 3 / 10 is 0.3
# The result of 12 * 19 is 228
# The result of 14 - 6 is 8
# The result of 3 * 88 is 264
# The result of 45 * 68 is 3060
# The result of 81 - 0 is 81
# The result of 77 + 40 is 117
# The result of 8 * 84 is 672
# The result of 73 - 22 is 51
# The result of 85 - 86 is -1
# The result of 28 * 58 is 1624


inp = open("E:\LabSection01_22101892_CSE221LabAssignment1_Summer2023\input1b.txt", "r")
out = open("E:\LabSection01_22101892_CSE221LabAssignment1_Summer2023\output1b.txt", "w")

n = int(inp.readline())

for i in range(n):
    line = inp.readline().split()

    if line[2] == "+":
        output = int(line[1]) + int(line[3])
    elif line[2] == "-":
        output = int(line[1]) - int(line[3])
    elif line[2] == "/":
        output = int(line[1]) / int(line[3])
    elif line[2] == "*":
        output = int(line[1]) * int(line[3])

    out.writelines(f"The result of {line[1]} {line[2]} {line[3]} is {output}\n")