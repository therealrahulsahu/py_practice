m, k = list(map(int, input().split()))
b = list(map(int, input().split()[:m]))
total = sum(b)
avg = total / k
time = [0]*k
out = [[] for _ in range(k)]

i = 0
left = 0
while b:
    book = b.pop(0)
    if time[i]+book > avg:
        left += (avg - time[i])
        if left >= book:
            left -= book
        else:
            i += 1

    if i == k:
        i = k-1

    out[i].append(book)
    time[i] += book

while out:
    res = out.pop(0)
    print(*res, end='')
    if len(out):
        print(' / ', end='')
    else:
        print()
