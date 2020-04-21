R, C, K, D = list(map(int, input().split()))
data = [tuple(map(int, input().split())) for _ in range(D)]
data.sort(key=lambda k: k[0])
distance = []
i = 0
X, Y = 0, 0
while i < D:
    j = i
    row = []
    while j < D:
        row.append((data[j][0]-X)+abs(data[j][1]-Y))
        j += 1
    distance.append(row)
    X, Y = data[i][0], data[i][1]
    i += 1


def s_path(grid, kill):
    if kill == 0:
        return 0
    else:
        return min([grid[0][i] + s_path(grid[i+1:], kill - 1) for i in range(len(grid)-kill+1)])


print(s_path(distance, K))

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