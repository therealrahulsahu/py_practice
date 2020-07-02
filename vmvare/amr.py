t = int(input())

def add_to_low(num, high, arr):
    count = 0
    result = []
    for x in arr:
        if x + num <= high:
            result.append(x + num)
            count += 1
        else:
            result.append(x)
    return (count, result)


def min_ops(coll):
    mx = max(coll)
    if len(set(coll)) == 1:
        return 0
    else:
        least = []
        loop = add_to_low(5, mx, coll)
        if loop[0]:
            coll = loop[1]
            least.append(min_ops(coll))

        loop = add_to_low(2, mx, coll)
        if loop[0]:
            coll = loop[1]
            least.append(min_ops(coll))

        loop = add_to_low(1, mx, coll)
        if loop[0]:
            coll = loop[1]
            least.append(min_ops(coll))

        return min(least) + 1

user = []
for _ in range(t):
    n = int(input())
    emps = list(map(int, input().split()))
    user.append(emps)

for x in user:
    print(min_ops(x))
