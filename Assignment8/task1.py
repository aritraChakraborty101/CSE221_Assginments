inp = open('input1_1.text', 'r')
out = open('output1_1.text', 'w')

# inp = open('input1_2.text', 'r')
# out = open('output1_2.text', 'w')

#####################################################

vertices, edges = map(int, inp.readline().split())

edge = []
weight = []

for i in range(edges):
    a, b, w = map(int, inp.readline().split())
    edge.append((a, b))
    weight.append(w)

# sort edges by weight


for i in range(edges):
    for j in range(edges - 1):
        if weight[j] > weight[j + 1]:
            weight[j], weight[j + 1] = weight[j + 1], weight[j]
            edge[j], edge[j + 1] = edge[j + 1], edge[j]


# create disjoint set

parent = [i for i in range(vertices + 1)]
rank = [0 for i in range(vertices + 1)]


def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def union(x, y):
    xroot = find(x)
    yroot = find(y)

    if xroot == yroot:
        return

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot

    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    else:
        parent[yroot] = xroot
        rank[xroot] += 1


# Kruskal's algorithm

def kruskal():
    mst = []
    i = 0
    e = 0

    while e < vertices - 1:
        u, v = edge[i]
        i += 1
        x = find(u)
        y = find(v)

        if x != y:
            e += 1
            mst.append((u, v))
            union(x, y)

    return mst


mst = kruskal()

result = 0

for u, v in mst:
    result += weight[edge.index((u, v))]


out.write(str(result))
