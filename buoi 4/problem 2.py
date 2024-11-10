n = int(input())
m = int(input())

a = [input() for i in range(n)]
b = [input() for i in range(m)]

c = []
for i in range(max(n, m)):
    if i < n:
        c.append(a[i])
    if i < m:
        c.append(b[i])

print(c) 