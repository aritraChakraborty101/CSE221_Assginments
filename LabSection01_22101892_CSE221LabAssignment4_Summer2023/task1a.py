inp = open("input1a_1.txt", "r")
out = open("output1a_1.txt", "w")

# inp = open("input1a_2.txt", "r")
# out = open("output1a_2.txt", "w")


# Reading the input file
first_line = inp.readline().split()

vertices = int(first_line[0])
edges = int(first_line[1])

# Creating a 2D array
result = [[0 for i in range(vertices + 1)] for j in range(vertices + 1)]

for i in range(edges):
    # Reading the input file
    arr = inp.readline().split()
    for j in range(len(arr)):
        arr[j] = int(arr[j])

    # Assigning the values to the variables
    node1 = arr[0]
    node2 = arr[1]
    weight = arr[2]

    # Adding the edges to the 2D array
    result[node1][node2] = weight

# Writing the output file
for i in range(0, vertices + 1):
    for j in range(0, vertices + 1):
        out.write(str(result[i][j]) + " ")
    out.write("\n")
