t = int(input())
ln = 0
num = 1
for _ in range(t):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    data.sort(key=lambda x: -x[0])

    for x in data:
        if x[num] % 2 == 1:
            x[num] -= 1

    result = 0
    carry = 0
    for x in data:
        if carry and x[num] >= 2:
            result += (carry*2 + x[ln]*2)
            x[num] -= 2
            carry = 0

        n_4 = x[num] // 4
        if n_4 > 0:
            result += x[ln] * 4 * n_4
            x[num] -= n_4 * 4

        if x[num] == 2:
            carry = x[ln]

    print(result)
