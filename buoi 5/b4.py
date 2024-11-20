import random

def taoTK(N):
    cn = ["CNTT", "KHMT", "KTPM", "HTTT", "DAPT"]
    acc = {}
    
    for i in range(N):
        student_id = 2023600000 + i
        password = random.choice(cn) + str(student_id)
        acc_name = f"Account{i + 1}"
        acc[acc_name] = {
            "Username": student_id,
            "Password": password
        } 
    return acc

N = int(input())
account_info = taoTK(N)
for account, info in account_info.items():
    print(f"{account}: {info}")
