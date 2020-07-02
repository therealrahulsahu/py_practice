n = int(input())
arr = list(map(int, input().split()))
f = arr[0]
least = 999999999
for i in arr[1:]:
    if i <= f:
        if least > f-i:
            least = f-i
print(least)
