R, C, K, D = list(map(int, input().split()))
data = [tuple(map(int, input().split())) for _ in range(D)]
data.sort(key=lambda k: k[0])
memo = {}


def s_path(grid, kill, x=0, y=0):
    if kill == 0:
        return 0
    else:
        try:
            return memo[str(x) + str(y) + str(kill)]
        except KeyError:
            upper = len(grid)-kill+1
            result = min([(grid[i][0]-x)+abs(grid[i][1]-y) + s_path(grid[i + 1:], kill - 1, grid[i][0], grid[i][1]) for i in range(upper)])
            memo[str(x)+str(y)+str(kill)] = result
            return result


print(s_path(data, K))

'''
10 10 5 7
1 7
3 6
5 1
6 5
7 4
4 3
2 2
'''