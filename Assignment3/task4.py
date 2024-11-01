# In this problem, you will be given a list of numbers. You have
# to find the k-th smallest value from the list without sorting
# using the Partition function of Quick sort.
# We will consider the 1 based indexing of the list.
#
# Input
# The first line contains an integer N (1 <= N <= 106), denoting
# the length of the list.
# The next line contains N integers A1,A2,............,An( 1 ≤ Ai ≤ 106)
# separated by a space.
# The third line contains a single integer Q (1 <= Q <= 100) -
# which denotes the number of queries you have to answer.
#
# Each of the next Q lines will contain a single integer K (1 ≤ K ≤ N).
#
# Output:
# For each query, you have to find the K-th smallest number from
# the given list.
#
# Sample Input/Output:
#
# Sample Input 1 Sample Output 1
# 9 // Total Elements
# 10 11 10 6 7 9 8 15 2
# 4 // Total queries
# 5
# 3
# 2
# 7
#
# 9
# 7
# 6
# 10

inp = open('input4.txt', 'r')
out = open('output4.txt', 'w')

n = int(inp.readline())
arr = inp.readline().split()

for i in range(n):
    arr[i] = int(arr[i])

queries = []  # list of queries
t = int(inp.readline())
for i in range(t):
    queries.append(int(inp.readline()))


# we have to find the k-th smallest value from the list without sorting
# using the Partition function of Quick sort.
# We will consider the 1 based indexing of the list.


def partition(arr, low, high):
    pivot = arr[high]  # pivot
    i = low - 1  # index of smaller element
    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


print(arr)
print(queries)
