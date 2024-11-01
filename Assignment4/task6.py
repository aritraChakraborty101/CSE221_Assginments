# inp = open("input6_1.txt", "r")
# out = open("output6_1.txt", "w")

inp = open("input6_2.txt", "r")
out = open("output6_2.txt", "w")

# inp = open("input6_3.txt", "r")
# out = open("output6_3.txt", "w")

# inp = open("input6_4.txt", "r")
# out = open("output6_4.txt", "w")

# inp = open("input6_5.txt", "r")
# out = open("output6_5.txt", "w")

# inp = open("input6_6.txt", "r")
# out = open("output6_6.txt", "w")

# inp = open("input6_7.txt", "r")
# out = open("output6_7.txt", "w")

#############################################

n, m = inp.readline().split()
n, m = int(n), int(m)

grid = []
for i in range(n):
    grid.append((inp.readline()).strip("\n"))


def dfs(grid, r, c, visited):
    # Check if the current cell is out of bounds or is a wall or is already visited
    # if either of these conditions is true, then return 0
    # 0 means that no diamonds are collected
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '#' or visited[r][c]:
        return 0

    visited[r][c] = True
    diamonds = 0

    if grid[r][c] == 'D':
        diamonds = 1

    # Recursively call dfs on the neighbors of the current cell
    diamonds += dfs(grid, r - 1, c, visited)
    diamonds += dfs(grid, r + 1, c, visited)
    diamonds += dfs(grid, r, c - 1, visited)
    diamonds += dfs(grid, r, c + 1, visited)

    return diamonds


def find_max_diamonds(grid):
    rows = len(grid)
    cols = len(grid[0])
    max_diamonds = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':  # If the current cell is empty
                visited = []
                # Create a visited matrix and initialize it with False
                # This means that no cell is visited yet
                for _ in range(rows):
                    visited.append([False] * cols)
                diamonds_collected = dfs(grid, r, c, visited)
                if diamonds_collected > max_diamonds:
                    max_diamonds = diamonds_collected

    return max_diamonds


# The main approach to solve this problem is to use DFS
# We will start from each empty cell and try to collect as many diamonds as possible
# We will keep track of the maximum number of diamonds collected
# And return it as the answer
# Time complexity: O(n * m)

####################################################


# main function call to find the maximum number of diamonds collected
out.write(str(find_max_diamonds(grid)))