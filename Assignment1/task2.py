# Task 2:
# Here is the code of bubble sort. Its run time complexity is θ(n
# 2
# ). Change the code in a
#
# way so that its time complexity is θ(n) for the best-case scenario.
# You have to explain how you have achieved the θ(n) for the best-case scenario in a
# comment block of your code.
# def bubbleSort(arr):
# for i in range(len(arr)-1):
# for j in range(len(arr)-i-1):
# if arr[j] > arr[j+1]:
# arr[j], arr[j+1] = arr[j+1], arr[j]
#
# Input 1:
# 5
# 3 2 1 4 5
#
# Output 1:
# 1 2 3 4 5
#
# Input 2:
# 6
# 5 10 15 20 25 30
#
# Output 2:
# 5 10 15 20 25 30
#
# For the input 2, your code should run at θ(n).


inp = open("E:\LabSection01_22101892_CSE221LabAssignment1_Summer2023\input2.txt", "r")
out = open("E:\LabSection01_22101892_CSE221LabAssignment1_Summer2023\output2.txt", "w")

n = inp.readline()
arr_line = inp.readline().split(" ")
n = int(n)
arr = []
for i in range(n):
    arr.append(int(arr_line[i]))

# From the concept of the bubble sort we know that it swaps variable only
# when it finds the next item smaller than the previous one. From this
# operation we can come to a conclusion. That is, if for an entire n length
# it does not find any item that bigger than its previous one , it will not perform any swap
# So, we can keep track of those swaps with a boolean variable then if it does not perform any swaps
# for an entire loop the code will terminate itself.
# In the best case if the input array is already sorted then the loop will terminate
# after n operation

for i in range(n):
    flag = False  # for keeping track of the swaps
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            flag = True  # If swap occurs it will give true

    if not flag:  # here it will terminate itself
        break

for i in range(n):
    out.writelines(f"{arr[i]} ")
