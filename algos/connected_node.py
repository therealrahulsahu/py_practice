ST = 0
END = 1
N, M, K = list(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(M)]
museum = tuple(map(int, input().split()))

connect_set = []
visited = [False]*(N+1)
for road in roads:
    found = False
    for xn_set in connect_set:
        if (road[ST] in xn_set) or (road[END] in xn_set):
            xn_set.add(road[ST])
            xn_set.add(road[END])
            visited[road[ST]] = True
            visited[road[END]] = True
            found = True
    if not found:
        connect_set.append({road[ST], road[END]})
        visited[road[ST]] = True
        visited[road[END]] = True

i = 1
while i <= N:
    if not visited[i]:
        connect_set.append({i})
    i += 1

result = []
for xn_set in connect_set:
    total = 0
    for node in xn_set:
        total += museum[node-1]
    result.append(total)
result.sort()

output = 0
if len(result) < K:
    print(-1)
else:
    i = 0
    while i < K:
        if i % 2:
            output += result.pop(0)
        else:
            output += result.pop()
        i += 1
    print(output)


