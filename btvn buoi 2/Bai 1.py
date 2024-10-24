a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

print("a + b = ", a + b)
print("a - b = ", a - b)
print(f"a * b = {a * b}")
print(f"a // b = {a // b}")
print(f"a ** b = {a ** b}")
print(f"a % b = {a % b}")

if a > b:
    print("a lon hon b")
elif a < b:
    print("a nho hon b")
else:
    print("a bang b")

print(f"a AND b = {a & b}")
print(f"a OR b = {a | b}")
print(f"a XOR b = {a ^ b}")
print(f"NOT a == b: {not a == b}")
print(f"a dich phai 5 bit: {a >> 5}")
print(f"a dich trai 6 bit: {a << 6}")

#chuyển a sang hệ nhị phân bang vong while
cs2 = ""
while a > 0:
    cs2 = str(a % 2) + cs2
    a = a // 2
    
cs2 = cs2[::-1]
print(f"co so 2 dao nguoc cua a: {cs2}")