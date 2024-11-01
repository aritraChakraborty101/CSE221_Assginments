# Your little brother, Alice, is very fond of playing with
# integers. One day, Alice was given a list of N integers by his
# school teacher. Now, your brother wants to play a game with you.
# Alice will give you an integer, S. You have to find if it is
# possible to find two values from the list (at distinct
# positions) whose sum is equal to S.
# Now you are feeling very tired. So you decided to write a code,
# so that it can give you the answer very quickly.
#
# 1) Can you write an O(n2) Solution to solve the problem?
# [Points 5]
# 2) Come up with an O(n) or O(nlogn) solution. [Points 10]
#
# Input
# The first line contains two integers N and S (1 <= N <= 105, 1 <=
# S <= 109), denoting the length of the list, and the target Sum.
# In the next line, there will be N integers a1,a2,............,aN(1 ≤ ai ≤
# 109) separated by space.
# Output
# Print two integers: the positions of the values [1 based
# indexing]. If there are several solutions, you may print any of
# them. If there are no solutions, print “IMPOSSIBLE”.
#
# Sample Input 1 Sample Output 1
# 4 10
# 3 7 1 5
#
# 1 2
#
# Sample Input 2 Sample Output 2
# 6 18
# 9 10 1 5 9 8
#
# 1 5
# [2 6 is also a valid answer]
# [print only one output]
#
# Sample Input 3 Sample Output 3
# 4 7
# 2 4 6 8
#
# IMPOSSIBLE
#
# Sample Input 4 Sample Output 4
# 3 12
# 6 1 2
#
# IMPOSSIBLE



inp = open("/workspaces/CSE221_Assginments/LabSection01_22101892_CSE221LabAssignment2_Summer2023/input1a.txt","r")
out = open("/workspaces/CSE221_Assginments/LabSection01_22101892_CSE221LabAssignment2_Summer2023/output1a.txt","w")


n, target = map(int, inp.readline().split())
arr = inp.readline().split()
for i in range(n):
    arr[i] = int(arr[i])

flag = False
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == target:
            out.write(str(i+1) + " " + str(j+1))
            flag = True
            break
    break

if not flag:
    out.write("IMPOSSIBLE")