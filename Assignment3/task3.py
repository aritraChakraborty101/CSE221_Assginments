# inp = open('input3_1.txt', 'r')
# out = open('output3_1.txt', 'w')

inp = open('input3_2.txt', 'r')
out = open('output3_2.txt', 'w')
#
# inp = open('input3_3.txt', 'r')
# out = open('output3_3.txt', 'w')

# inp = open('input3_4.txt', 'r')
# out = open('output3_4.txt', 'w')

n = int(inp.readline())
arr = inp.readline().split()

for i in range(n):
    arr[i] = int(arr[i])

###############################################

# performing quick sort
# First element is pivot element in this case (arr[l])
# l - left border of array
# r - right border of array
# m - index of pivot element after partition
# x - pivot element
# i - index of element in array
# j - index of last element less or equal to pivot element

# After partitioning array looks like this:
# [elements less than pivot] [pivot] [elements greater than pivot]
# [arr[l] ... arr[j]] [arr[j + 1]] [arr[j + 2] ... arr[r]]
# Time complexity: O(nlogn) in average case, O(n^2) in worst case
# Space complexity: O(logn) in average case, O(n) in worst case

def quick_sort(arr, l, r):
    if n == 1:
        return arr
    if l >= r:
        return arr
    m = partition(arr, l, r)
    quick_sort(arr, l, m - 1)
    quick_sort(arr, m + 1, r)
    return arr

# Partitioning array
# Time complexity: O(n)
# Space complexity: O(1)

# The partition function takes the first element as pivot element
# and places it in the correct position in the array.
# It also places all elements less than pivot to the left of pivot
# and all elements greater than pivot to the right of pivot.
# It returns the index of pivot element after partitioning.

def partition(arr, l, r):
    x = arr[l]  # pivot element
    j = l  # index of last element less or equal to pivot
    for i in range(l + 1, r + 1):
        if arr[i] <= x:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


# Calling the Quick Sort function
arr = quick_sort(arr, 0, n - 1)

for i in range(n):
    out.write(str(arr[i]) + ' ')

inp.close()
out.close()