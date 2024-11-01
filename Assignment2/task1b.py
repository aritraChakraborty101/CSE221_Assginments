
inp = open("E:\LabSection01_22101892_CSE221LabAssignment2_Summer2023\input1b.txt","r")
out = open("E:\LabSection01_22101892_CSE221LabAssignment2_Summer2023\output1b.txt","w")


n, target = map(int, inp.readline().split())
arr = inp.readline().split()
for i in range(n):
    arr[i] = int(arr[i])

main_arr = arr.copy()

# The following program contains the necessary functions such as merge_sort, merge and binary_search
# to solve the problem in O(nlogn) time complexity and O(1) space complexity

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    first_arr = [0] * n1
    second_arr = [0] * n2

    for i in range(0, n1):
        first_arr[i] = arr[left + i]

    for j in range(0, n2):
        second_arr[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

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


def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def binary_search(arr, low, high, searchKey):

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == searchKey:
            return 1
        if arr[mid] < searchKey:
            low = mid + 1
        else:
            high = mid - 1

    return 0


# The following program contains the solution of the problem in O(nlogn) time complexity
# and O(n) space complexity
# First the program copy the main array into another array to keep track of the original indices of the elements
# This program first sorts the given array using merge sort algorithm
# Then it uses binary search to find the pair of elements whose sum is equal to the target sum
# if it finds such a pair, it breaks the loop and search that element in the main array
# Otherwise, it prints "IMPOSSIBLE"
# The binary search, merge sort algorithms and index() function have O(logn), O(nlogn) and O(n)
# time complexities respectively
# So, the overall time complexity of the program is O(nlogn)

merge_sort(arr, 0, n - 1)
flag = False

for i in range(n - 1):
    searchKey = target - arr[i]
    if binary_search(arr, i + 1, n - 1, searchKey) == 1:
        first_idx = main_arr.index(arr[i]) + 1
        second_idx = main_arr.index(searchKey) + 1
        out.write(str(first_idx) + " " + str(second_idx))
        flag = True
        break

if not flag:
    out.write("IMPOSSIBLE")


