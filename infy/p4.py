from re import compile
reg = compile(r'99')
n = int(input())
data = [input() for _ in range(n)]

i = 0
output = 0
while i < n:
    if reg.search(data[i]):
        output += (2**i)
    i += 1

print(output)
