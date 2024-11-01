# inp = open('input3_1.text', 'r')
# out = open('output3_1.text', 'w')

inp = open('input3_2.text', 'r')
out = open('output3_2.text', 'w')
###############################################
# The main idea is to use the DSU data structure
# to store the number of people in each group
# and then to print the number of people in the
# group of the person
###############################################
first_line = inp.readline().split()
people = int(first_line[0])
tasks = int(first_line[1])

query = []

for i in range(tasks):
    tmp = inp.readline().split()
    query.append([int(tmp[0]), int(tmp[1])])


parent = [None] * (people + 1)
size = [1] * (people + 1)


def make_set(x):
    parent[x] = x


def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        size[x] += size[y]


for i in range(people + 1):
    make_set(i)

for i in range(tasks):
    union(query[i][0], query[i][1])
    out.write(str(size[find(query[i][0])]) + '\n')



