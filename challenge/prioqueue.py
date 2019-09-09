n = int(input('Enter n : '))
data = list(map(int, input('Enter Array : ').split()[:n]))
k = int(input('Enter k :'))
my_pri = data[k]
dt_ind = []
i = 0
for x in data:
    dt_ind.append((i, x))
    i += 1

time = 0
while True:
    mx = max(dt_ind, key=lambda x: x[1])
    while dt_ind[0][1] < mx[1]:
        dt_ind.append(dt_ind.pop(0))

    time += 1
    if dt_ind[0][0] == k:
        break
    else:
        dt_ind.pop(0)
print(time)
