registered = set(input().split())
checked = set(input().split())

not_checked = registered - checked
print(not_checked)

total = registered | checked
print(total)

print(sorted(registerd))