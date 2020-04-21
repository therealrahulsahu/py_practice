m, k = list(map(int, input().split()))
b = list(map(int, input().split()[:m]))*10
k = 13

total = sum(b)
avg = total / k
time = [0]*k
out = [[] for _ in range(k)]

i = 0
left = 0
while b:
    book = b.pop(0)
    if time[i]+book > avg:
        i += 1

    if i == k:
        i = k-1

    out[i].append(book)
    time[i] += book

every = False
while not every:
    any = False
    i = len(out) - 1
    while i > 0:
        if sum(out[i][1:]) < avg:
            i -= 1
        else:
            l = out[i-1]
            r = out[i]
            l.append(r.pop(0))
            any = True
    if not any:
        every = False

for x in out:
    print(sum(x), end=' ')
print()

while out:
    res = out.pop(0)
    print(*res, end='')
    if len(out):
        print(' / ', end='')
    else:
        print()
