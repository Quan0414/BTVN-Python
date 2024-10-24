print("Chao mung den CLB Tin Hoc HIT")
print("CLB Tin Hoc HIT truc thuoc Khoa CNTT  - 10 diem")

#----------------------------------------------
s = "CLB Tin Hoc HIT truc thuoc Khoa CNTT "
print("Cac chu in hoa: ", end="")
for i in s:
    if i.isupper():
        print(i, end="")
print()
print("Cac chu thuong: ", end="")
for i in s:
    if i.islower():
        print(i, end="")
print()

#----------------------------------------------
print("Yes" if "CNTT" in s else "No")

#----------------------------------------------
s = "CLB Tin Hoc HIT truc thuoc Khoa CNTT "
s = s.swapcase()
print(s)
