# inp = open('input3_1.text', 'r')
# out = open('output3_1.text', 'w')

inp = open('input3_2.text', 'r')
out = open('output3_2.text', 'w')

############################################

n, x = map(int, inp.readline().split())
a = list(map(int, inp.readline().split()))

############################################

# here we are given a target sum x and some numbers
# we have to find the minimum number of numbers required to get the sum x


# we will use the concept of dynamic programming
# we will create a 2d array of size n+1 and x+1
# dp[i][j] will store the minimum number of numbers required to get the sum j using the first i numbers

def min_coin(a, n, x):
    dp = [[0 for j in range(x+1)] for i in range(n+1)]

    for i in range(1, x+1):
        dp[0][i] = float('inf')

    for i in range(1, n+1):
        for j in range(1, x+1):
            dp[i][j] = dp[i-1][j]
            if j >= a[i-1]:
                dp[i][j] = min(dp[i][j], 1 + dp[i][j-a[i-1]])

    return dp[n][x]

############################################


if min_coin(a, n, x) == float('inf'):
    out.write('-1')
else:
    out.write(str(min_coin(a, n, x)))

############################################

inp.close()
out.close()

