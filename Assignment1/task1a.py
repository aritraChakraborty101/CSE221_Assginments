# a) You are given a file “input1a.txt”. The first line of the input file will contain an integer T,
# representing the number of test cases. The next T lines will contain an integer N. You
# have to calculate if the number is Odd or Even. For each test case print the expected
# output. All the results must be compiled in a single file, “output1a.txt.”
# Sample Input File Sample Output File
# 5
# 10
# 19
# 7
# 3
# 100
#
# 10 is an Even number.
# 19 is an Odd number.
# 7 is an Odd number.
# 3 is an Odd number.
# 100 is an Even number.
#
# b) You are given a file “input1b.txt”. The first line of the input file will contain an integer T,
# representing the number of test cases. The next T lines will contain a single arithmetic
# expression. Each arithmetic expression will start with the prefix “calculate“. It is
# guaranteed that the expression will have exactly two operands and one operator.
# Calculate the result of each expression. Your output format should exactly match with
# the sample output format. All the results must be compiled in a single file,
# “output1b.txt.”

inp = open("E:\LabSection01_22101892_CSE221LabAssignment1_Summer2023\input1a.txt", "r")
out = open("E:\LabSection01_22101892_CSE221LabAssignment1_Summer2023\output1a,txt", "w")

n = inp.readline()
n = int(n)

for i in range(n):
    num = int(inp.readline())
    if num % 2 == 0:
        out.writelines(str(num) + " is an Even number.\n")
    else:
        out.writelines(str(num) + " is an Odd number.\n")