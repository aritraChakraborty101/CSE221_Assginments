# Somewhere in the universe, the Biannual Regional Alien
# Competition is taking place.
# There are N aliens standing in a line. You will be given a
# permutation of N, which denotes the height of each alien. A
# sequence of N numbers is called permutation if it contains all
# integers from 1 to N exactly once. For example, the sequences
# [3,1,4,2], [1] and [2,1] are permutations, but [1,2,1], [0,1]
# and [1,3,4] — are not.
# In the competition, for each alien, the judge wants to count how
# many aliens are standing on its right side with a strictly
#
# smaller height. The judge writes the following code to solve the
# problem.
#
# count = 0
# for i in range(n):
# for j in range(i+1,n):
# if H[i] > H[j]:
# count+=1
#
# However, their algorithm wasn’t efficient at all. Hence, the
# alien calls you to write a better solution for the program.
# More formally, you have to count how many pairs of aliens are
# standing in the line such that H[i] > H[j] and i<j. Here, A is
# the permutations of Alience’s height. And i,j denotes the
# Alience’s position.
#
# Input
# The first line contains a single integer 1 <= N <= 106 - the
# number of total aliens.
# The next line contains N integers H1,H2,............,Hn(1 ≤ Hi ≤ N)- the
# height of the i-th alien. It is guaranteed that the given heights will
# be the permutation of N.
#
# Output
# Print a single integer, which denotes the total number of
# inversions of the given permutation of alien’s heights as
# described in the problem statement.
#
# Sample Input/Output:
# Sample Input 1 Sample Output 1
# 5
# 1 2 3 4 5
#
# 0
#
# Sample Input 2 Sample Output 2
# 5
# 5 4 3 2 1
#
# 10
#
# Sample Input 3 Sample Output 3
# 8
# 2 7 4 1 5 6 8 3
#
# 11
#
# Sample Input 3 Explanation:
# In the sample input 3, the following pairs on alien’s heights
# satisfy the condition: (2,1), (7,4), (7,1), (7,5), (7,6), (7,3),
# (4,1), (4,3), (5,3), (6,3), (8,3)


###################################################

# All the input and output files are included below

# inp = open('input1_1.txt', 'r')
# out = open('output1_1.txt', 'w')

# inp = open('input1_2.txt', 'r')
# out = open('output1_2.txt', 'w')
#
inp = open('input1_3.txt', 'r')
out = open('output1_3.txt', 'w')


n = int(inp.readline())
arr = inp.readline().split()
arr = [int(i) for i in arr]
###############################################

count = 0

# Here we will use the divide and conquer approach
# We will divide the array into two parts and then
# count the number of inversions in the left and right
# sub arrays and then count the number of inversions
# between the two sub arrays


def merge(arr, count, left, mid, right):
    tmp = []  # temporary array to store the sorted array
    i = left  # pointer to the left subarray
    j = mid + 1  # pointer to the right subarray
    k = 0  # pointer to the temporary array

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
            count += mid - i + 1

    while i <= mid:
        tmp.append(arr[i])
        i += 1

    while j <= right:
        tmp.append(arr[j])
        j += 1

    for i in range(left, right + 1):
        arr[i] = tmp[i - left]

    return count


def merge_sort(arr, count, left, right):
    if left >= right:
        return count

    mid = (left + right) // 2
    count = merge_sort(arr, count, left, mid)
    count = merge_sort(arr, count, mid + 1, right)
    count = merge(arr, count, left, mid, right)
    return count


def count_inversions(arr, count, n):
    return merge_sort(arr, count, 0, n - 1)


count = count_inversions(arr, count, n)
out.write(str(count))
inp.close()
out.close()



