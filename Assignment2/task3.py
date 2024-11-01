inp = open("E:\LabSection01_22101892_CSE221LabAssignment2_Summer2023\input3.txt", "r")
out = open("E:\LabSection01_22101892_CSE221LabAssignment2_Summer2023\output3.txt", "w")

# Reading the input file
n = int(inp.readline())
arr = inp.readline().split(" ")
arr = [int(i) for i in arr] # Converting the string array to integer array


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
arr = mergeSort(arr)
for i in range(n):
    out.write(str(arr[i]) + " ")