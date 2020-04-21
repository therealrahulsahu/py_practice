R, C, K, D = list(map(int, input().split()))
data = [tuple(map(int, input().split())) for _ in range(D)]
data.sort(key=lambda k: k[0])
MAX = 999999999


def s_path(grid, kill, x=0, y=0):
    if kill == 0:
        return 0
    min_path = MAX
    min_index = None
    i = 0
    upper = len(grid)-kill+1
    while i < upper:
        n_path = (grid[i][0]-x) + abs(grid[i][1]-y)
        if n_path < min_path:
            min_path = n_path
            min_index = i
        i += 1
    return min_path + s_path(grid[min_index+1:], kill-1, grid[min_index][0], grid[min_index][1])


print(s_path(data, K))
