n = int(input())
m = int(input())

A = tuple(int(input()) for i in range(n))
B = tuple(input() for i in range(m))

avg = sum(A) / n
cnt = 0
for i in range(A):
    if A[i] > avg:
        cnt += 1
print(cnt)

evenA = tuple(x for x in A if x % 2 == 0)
oddA = tuple(x for x in A if x % 2 == 1)

k = input()
k_in_B = B.count(k)

new_B = tuple(x for x in B if len(x) > 5)

min_length = min(len(A), len(B))
C = tuple((A[i], B[i]) for i in range(min_length))