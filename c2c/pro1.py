from itertools import combinations as comb
n,a,b,c,d = map(int,input().split())
data = [i for i in range(a,b+1)]
result = 0
arrlen = b-a+1
for i in range(c,d+1):
    temp = set(data)
    for j in range(1,n+1):
        subset = 6

