def solve(coded_str):
    stack = []
    cur_num = 0
    cur_str = ''
    
    for char in coded_str:
        if char.isdigit():
            cur_num = int(char)
        elif char == '[':
            stack.append((cur_str, cur_num))
            cur_str = ''
            cur_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            cur_str = prev_str + cur_str * num
        else:
            cur_str += char

    return cur_str

s = input()
print(solve(s))