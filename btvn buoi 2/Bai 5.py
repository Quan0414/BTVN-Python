a = int(input("Nhap so a: "))
cs8 = ""
while a > 0:
    cs8 = str(a % 8) + cs8
    a = a // 8

print(f"So bit can de bieu dien: {len(cs8) * 3}")

print(dir(a))
