m = int(input())
n = int(input())

num_list1 = [int(input()) for i in range(m)]
num_list2 = [int(input()) for i in range(n)]

result = []

for i in num_list1:
    if i in num_list2:
        result.append(num)
        nums2.remove(num)

print(result)