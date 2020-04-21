from itertools import combinations as cb

R, C, K, D = list(map(int, input().split()))
data = [tuple(map(int, input().split())) for _ in range(D)]


data.sort(key=lambda x: x[0])
result = []
for case in cb(data, K):
    X, Y = 0, 0
    steps = 0
    for X1, Y1 in case:
        steps += X1-X + abs(Y1-Y)
        X = X1
        Y = Y1
    result.append(steps)

print(min(result))
