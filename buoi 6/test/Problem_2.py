def count(word):
    cnt = {}  
    for i in word:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    
    return cnt

s = input()
result = count(s)
result = dict(sorted(result.items()))
print(result)