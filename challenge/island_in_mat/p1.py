def all_nearby(x, y, x_max, y_max):
    # Returns all nearby nodes
    near = [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y), (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
    ]
    if (0 <= x < x_max) and (0 <= y < y_max):
        result = [point for point in near if (0 <= point[0] < x_max) and (0 <= point[1] < y_max)]
    else:
        result = []
    return result


def all_connected(grid, memo, x, y, x_max, y_max, mark):
    # Returns list of all connected nodes and make changes in memoization table
    if (0 <= x < x_max) and (0 <= y < y_max) and grid[x][y]:
        stack = [(x, y)]
        result = [(x, y)]
        memo[x][y] = mark
        while stack:
            i, j = stack.pop()
            memo[i][j] = mark
            for point in all_nearby(i, j, x_max, y_max):
                if (memo[point[0]][point[1]] == -1) and grid[point[0]][point[1]]:
                    stack.append((point[0], point[1]))
                    result.append((point[0], point[1]))
        return result
    else:
        return []


def count_nodes(grid):
    memo = [[-1 for _ in range(C)] for _ in range(R)]
    count = 0
    for i in range(0, R):
        for j in range(0, C):
            if data[i][j] == 0:
                memo[i][j] = 0
            elif data[i][j] == 1 and memo[i][j] == -1:
                output = all_connected(grid, memo, i, j, R, C, count+1)
                count += 1
    return count
    # print memo table to get all connected nodes at once


R, C = 10, 5
data = [
    [1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0]
]

print(count_nodes(data))
