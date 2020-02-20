S = 0
E = 1
I = 2
C, N, K = list(map(int, input().split()))
data = []
for x in range(N):
  ls = list(map(int, input().split()))
  data.append([ls[0], ls[1], x])
data.sort(key=lambda x: (x[0], x[1]))

result = True
i = 0
conf = 0

while i < N - 1:
    j = i + 1
    while j < N:
        if data[i][E] >= data[j][S]:
            conf += 1
        else:
            break
        j += 1
    i += 1

if K:
    if conf == 0:
        result = True
    elif conf == 2:
        result = False
    elif conf == 1:
        result = False
else:
    if conf:
        result = False
    else:
        result = True

if result:
    print("Good")
else:
    print("Bad")
