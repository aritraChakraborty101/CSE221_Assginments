# The following function is the implementation of the divide and
# conquer approach to find out the maximum number from the given
# list.
# Time Complexity: O(n)

def findMax(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    max1 = findMax(arr, low, mid)
    max2 = findMax(arr, mid + 1, high)
    if max1 > max2:
        return max1
    else:
        return max2

inp = open("E:\LabSection01_22101892_CSE221LabAssignment2_Summer2023\input4.txt", "r")
out = open("E:\LabSection01_22101892_CSE221LabAssignment2_Summer2023\output4.txt", "w")
n = int(inp.readline())
arr = inp.readline().split()
for i in range(n):
    arr[i] = int(arr[i])

out.write(str(findMax(arr, 0, n - 1)))