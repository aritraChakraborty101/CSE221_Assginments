inp = open("E:\LabSection01_22101892_CSE221LabAssignment2_Summer2023\input2a.txt", "r")
out = open("E:\LabSection01_22101892_CSE221LabAssignment2_Summer2023\output2a.txt", "w")

# Reading the input file
n1 = int(inp.readline())
arr1 = inp.readline().split()
first_arr = [int(i) for i in arr1] # Converting the string array into integer array

n2 = int(inp.readline())
arr2 = inp.readline().split()
second_arr = [int(i) for i in arr2]

# The following code is for takes two arrays and merge them into one sorted array
# The time complexity of this code is O(nlogn)
# Firstly it takes two array and add them into one array
# Then it sorts the array using merge sort algorithm
# Finally it prints the sorted array


def merge(a, b):
    c = [0] * (len(a) + len(b))
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        c[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1
    return c

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)


# Calling the mergeSort function
arr = merge(first_arr, second_arr)
arr = mergeSort(arr)
for i in range(n1 + n2):
    out.write(str(arr[i]) + " ")