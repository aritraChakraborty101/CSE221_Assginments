# inp = open('input2_1.text', 'r')
# out = open('output2_1.text', 'w')

# inp = open('input2_2.text', 'r')
# out = open('output2_2.text', 'w')

# inp = open('input2_3.text', 'r')
# out = open('output2_3.text', 'w')

inp = open('input2_4.text', 'r')
out = open('output2_4.text', 'w')

############################################
# The idea is to store the results of the problems so that we do not have to re-compute them when needed later.
# Instead of recursion, we can also solve the above problem iteratively. The idea is similar, we only need to store
# the last two results of the problems and compute the result of the current problem. This can be easily done
# by storing the last two results in two variables and updating them for each iteration.

# Time Complexity: O(n)
############################################
n = int(inp.readline())


def count_ways2(n):
    table = [0] * (n + 1)
    table[1] = 1
    table[2] = 2
    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]


out.write(str(count_ways2(n)))




