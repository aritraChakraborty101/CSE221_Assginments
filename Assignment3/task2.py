# You are given a list of integers. You have to choose two indices
# i and j such that A[i] + A[j]2 is maximum possible (1 <= i < j
# <= N, where N is the length of the given list). Here, we are
# considering 1 based indexing.
# Write a code which will find the maximum value of A[i] + A[j]2
# in O(N) or O( N log N).
#
# Input
# The first line contains a single integer 1 <= N <= 106 - the
# length of the list.
# The next line contains N integers A1,A2,............,An (-108 ≤ Ai ≤ 108)
# separated by a space.
#
# Output
# Print a single integer - which denotes the maximum possible
# value of A[i] + A[j]2.
#
# Sample Input/Output:
# Sample Input 1 Sample Output 1
# 5
# 9 6 5 8 2
#
# 73
#
# Sample Input 2 Sample Output 2
# 8
# 5 10 4 -3 1 6 -10 2
#
# 110
#
# Sample Input 3 Sample Output 3
# 7
# -5 -2 -6 -7 -1 8 2
#
# 63

#############################################
# inp = open('input2_1.txt', 'r')
# out = open('output2_1.txt', 'w')

inp = open('input2_2.txt', 'r')
out = open('output2_2.txt', 'w')
#
# inp = open('input2_3.txt', 'r')
# out = open('output2_3.txt', 'w')

#############################################


n = int(inp.readline())
arr = [int(i) for i in inp.readline().split()]
arr = [(arr[i], i) for i in range(len(arr))]
max_sum = 0
maxi = arr[1][0]
index = 1
for i in range(1, len(arr)):
    if abs(arr[i][0]) >= abs(maxi):
        maxi = arr[i][0]
        index = arr[i][1]

for i in range(index):
    if (arr[i][0] + maxi**2) > max_sum:
        max_sum = arr[i][0] + maxi**2

print(max_sum)
out.writelines(f"{max_sum}")

