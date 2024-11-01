# inp = open('input1_1.text', 'r')
# out = open('output1_1.text', 'w')

# inp = open('input1_2.text', 'r')
# out = open('output1_2.text', 'w')

inp = open('input1_3.text', 'r')
out = open('output1_3.text', 'w')


n = int(inp.readline())
arr = [[] * n for i in range(n)]

for i in range(n):
    arr[i] = list(map(int, inp.readline().split()))


# sort by second element
# the main idea is to sort the array by the second element
# and then to check if the first element of the next pair is
# greater than the second element of the previous pair
# if it is, then we add the pair to the result array


arr.sort(key=lambda x: x[1])


result = []
result.append(arr[0])

for i in range(1, n):
    if arr[i][0] >= result[-1][1]:
        result.append(arr[i])


out.write(str(len(result)) + '\n')
for i in range(len(result)):
    out.write(str(result[i][0]) + ' ' + str(result[i][1]) + '\n')

