n = 100
ans = 1

def gt(n):
    if n == 0:
        return 1
    return n * gt(n - 1)

x = float(input())

for i in range(1, n + 1):
    ans += (x ** i) / gt(i)

print(ans)