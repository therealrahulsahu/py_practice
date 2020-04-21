def get_last(b, k):
    data = b.copy()
    total = sum(data)
    avg = total / k
    time = [0] * k
    out = [[] for _ in range(k)]

    i = 0
    left = 0
    while data:
        book = data.pop(0)
        if time[i] + book > avg:
            left += (avg - time[i])
            if left >= book:
                left -= book
            else:
                i += 1

        if i == k:
            i = k - 1

        out[i].append(book)
        time[i] += book
    return out[-1]


m, k = list(map(int, input().split()))
b = list(map(int, input().split()[:m]))

out = []
proc = 0
for i in range(k, 0, -1):
    if proc:
        last = get_last(b[:-proc], i)
    else:
        last = get_last(b, i)
    proc += len(last)
    out.insert(0, last)


while out:
    res = out.pop(0)
    print(*res, end='')
    if len(out):
        print(' / ', end='')
    else:
        print()
