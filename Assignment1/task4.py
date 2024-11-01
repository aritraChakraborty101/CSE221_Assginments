# Task 4:
# You have been recently recruited as the Software Engineer at Jumanji Railway Software
# System. You have a big task at hand. You will be given the N ( 1 ≤ N ≤ 100 ) schedule of
# the train. The next N line will contain the name of the train and the departure time. See
# the input format for better understanding.
# Your task is to write a sorting algorithm that will group the trains in the lexicographical
#
# order based on the name of the trains. If two or more trains have the same name, then
# the train with the latest departure time will get prioritized. If there is still a tie, then the
# train which comes first in the input file will come first.
#
# Sample Input Sample Output
# 13
# ABCD will departure for Mymensingh at 00:30
# DhumketuExpress will departure for Chittagong at 02:30
# SubornoExpress will departure for Chittagong at 14:30
# ABC will departure for Dhaka at 17:30
# ShonarBangla will departure for Dhaka at 12:30
# SubornoExpress will departure for Rajshahi at 14:30
# ABCD will departure for Chittagong at 01:00
# SubornoExpress will departure for Dhaka at 11:30
# ABC will departure for Barisal at 03:00
# PadmaExpress will departure for Chittagong at 20:30
# ABC will departure for Khulna at 03:00
# ABCE will departure for Sylhet at 23:05
# PadmaExpress will departure for Dhaka at 19:30
#
# ABC will departure for Dhaka at 17:30
# ABC will departure for Barisal at 03:00
# ABC will departure for Khulna at 03:00
# ABCD will departure for Chittagong at 01:00
# ABCD will departure for Mymensingh at 00:30
# ABCE will departure for Sylhet at 23:05
# DhumketuExpress will departure for Chittagong at 02:30
# PadmaExpress will departure for Chittagong at 20:30
# PadmaExpress will departure for Dhaka at 19:30
# ShonarBangla will departure for Dhaka at 12:30
# SubornoExpress will departure for Chittagong at 14:30
# SubornoExpress will departure for Rajshahi at 14:30
# SubornoExpress will departure for Dhaka at 11:30
#
# Please note, you have to take the input from an input4.txt file, and show the
# output in an output4.txt file.

inp = open("E:\LabSection01_22101892_CSE221LabAssignment1_Summer2023\input4.txt", "r")
out = open("E:\LabSection01_22101892_CSE221LabAssignment1_Summer2023\output4.txt", "w")


n = inp.readline()
n = int(n)
result = []
for i in range(n):
    line = inp.readline()
    result.append(line)

result.sort()

for i in range(len(result)):
    out.writelines(f"{result[i]}\n")