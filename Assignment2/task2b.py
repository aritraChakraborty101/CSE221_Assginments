inp = open("E:\LabSection01_22101892_CSE221LabAssignment2_Summer2023\input2b.txt", "r")
out = open("E:\LabSection01_22101892_CSE221LabAssignment2_Summer2023\output2b.txt", "w")

# Reading the input file
n1 = int(inp.readline())
arr1 = inp.readline().split()
first_arr = [int(i) for i in arr1]

n2 = int(inp.readline())
arr2 = inp.readline().split()
second_arr = [int(i) for i in arr2]

# The following code is for takes two arrays and merge them into one sorted array
# The time complexity of this code is O(n1 + n2)
# It uses three pointers to keep track of the elements of the two arrays
# The first pointer is for the first array, the second pointer is for the second array
# The third pointer is for the merged array
# The first two pointers are used to compare the elements of the two arrays
# The third pointer is used to keep track of the merged array
# The while loops are used to merge the two arrays
# The last three while loops are used to merge the remaining elements of the two arrays


# Merging the two arrays
arr = [0] * (n1 + n2)
i = 0
j = 0
k = 0

while i < n1 and j < n2:
    if first_arr[i] <= second_arr[j]:
        arr[k] = first_arr[i]
        i += 1
    else:
        arr[k] = second_arr[j]
        j += 1
    k += 1

while i < n1:
    arr[k] = first_arr[i]
    i += 1
    k += 1

while j < n2:
    arr[k] = second_arr[j]
    j += 1
    k += 1

for i in range(n1 + n2):
    out.write(str(arr[i]) + " ")


