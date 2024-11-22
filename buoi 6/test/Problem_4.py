def solve(data):
    result = {}
    for item in data:
        pairs = item.split(';')
        for pair in pairs:
            key, value = pair.split('=')
            if key not in result:
                result[key] = []
            result[key].append(value)
    return result

data = ["name=Alice;age=30;score=85.5" ,
        "name=Bob;age =25;score=90" ,
        "name=Alice;age=30;score=92" ,
        "city=NewYork;name=Eve;age=35;score=88" ,
        "city=London;name=Alice;age=30;score=85.5"]
print(f"dict = {solve(data)}") 