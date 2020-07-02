# bonney 100
with open('p1.py', 'r') as file:
    n, l = list(map(int, file.readline().split()))
    data = {}
    for i in range(n):
        temp = list(map(int, file.readline().split()))
        d = temp[0]
        data[i] = []
        for st in temp[2:]:
            data[i].append((st, st + d))

'''n, l = list(map(int, input().split()))
data = {}
for i in range(n):
    temp = list(map(int, input().split()))
    d = temp[0]
    data[i] = []
    for st in temp[2:]:
        data[i].append((st, st+d))
'''

time = 0
count = 0
trave = []

while True:
    if time > l:
        break
    queue = []
    for ind in data:
        if ind not in trave:
            for y in data[ind]:
                if y[0] <= time < y[1]:
                    queue.append((ind, y))
    if queue:
        max_v = max(queue, key=lambda x: x[1][1])
        count += 1
        time = max_v[1][1]
        trave.append(max_v[0])
    else:
        count = -1
        break
print(count)
