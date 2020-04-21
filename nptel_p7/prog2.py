R, C, K, D = list(map(int, input().split()))
memo = [-1 for _ in range(R)]
data = [-1 for _ in range(R)]
for _ in range(D):
    inp = list(map(int, input().split()))
    data[inp[0]] = inp[1]
MAX = 999999999


def m_steps(kill, x=-1):
    if x != -1 and memo[x] != -1:
        pass
        #return memo[x]
    if kill == 0:
        return 0
    mn = MAX
    mn_ind = None
    i = x+1
    while i < R:
        if data[i] != -1:
            st = m_steps(kill-1, i)
            if st < mn:
                mn = st
                mn_ind = i
        i += 1
    if mn_ind is not None:
        if x != -1:
            result = mn + abs(mn_ind - x) + abs(data[mn_ind] - data[x])
            memo[x] = result
        else:
            result = mn + abs(mn_ind - 0) + abs(data[mn_ind] - 0)
            memo[0] = result
        return result
    else:
        return MAX


print(m_steps(K))
