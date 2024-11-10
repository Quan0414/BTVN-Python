k = int(input())
a = [int(input()) for i in range(k)]

m = int(input())
n = int(input())

if len(a) < n * m:
        print("Khong tao duoc ma tran")
else:
    ma_tran = [a[i * m:(i + 1) * m] for i in range(n)]
    print(ma_tran)