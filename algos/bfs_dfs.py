class City:
    def __init__(self, city_id, m_count):
        self.city_id = city_id
        self.connected = []
        self.n_museum = m_count

    def add(self, city):
        self.connected.append(city)


def first_false(visit):
    i = 0
    result = 0
    while i < len(visit):
        if not visit[i]:
            result = i
            break
        i += 1
    return result if i < len(visit) else -1


ST = 0
END = 1
N, M, K = list(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(M)]
museum = tuple(map(int, input().split()))

city_list = [City(x, museum[x]) for x in range(N)]
for x in roads:
    city_list[x[ST]-1].add(x[END]-1)

visited = [False]*N

bfs = []
nodes_museum = []
to_start = first_false(visited)
while to_start != -1:
    total = 0
    bfs += city_list[to_start].connected
    total += city_list[to_start].n_museum
    visited[to_start] = True
    while bfs:
        item = bfs.pop(0)
        total += city_list[item].n_museum
        visited[item] = True
        for node in city_list[item].connected:
            if not visited[node]:
                bfs.append(node)
    nodes_museum.append(total)
    to_start = first_false(visited)

if len(nodes_museum) < K:
    print(-1)
else:
    output = 0
    i = 1
    while i <= K:
        if i % 2:
            output += nodes_museum.pop(nodes_museum.index(max(nodes_museum)))
        else:
            output += nodes_museum.pop(nodes_museum.index(min(nodes_museum)))
        i += 1
    print(output)
