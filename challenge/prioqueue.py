def rotate(arr):
    var = arr.pop(0)
    arr.append(var)


n = int(input('Enter n : '))
data = list(map(int, input('Enter Array : ').split()[:n]))
k = int(input('Enter k :'))
my_pri = data[k]
dt_ind = []
i = 0
for x in data:
    dt_ind.append((i, x))
    i += 1
dist_pri = sorted(list(set(data)), reverse=True)
# print(*dt_ind, sep='\t')
time = 0
while True:
    mx = max(dt_ind, key=lambda x: x[1])
    first = dt_ind[0]
    if first[1] < mx[1]:
        rotate(dt_ind)
    else:
        time += 1
        if first[0] == k:
            break
        else:
            dt_ind.pop(0)
print(time)