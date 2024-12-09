with open('two.txt') as f:
    data = f.readlines()
    data = [item.strip().split(' ') for item in data]
    data = list(map(lambda x: list(map(int, x)), data))
    
sum = 0

def is_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    
def is_descending(lst):
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

def safe_check(data):
    sum = 0
    unsafes = []
    
    value = None
    safe = False
    for i in range(len(data)):
        d_copy = data.copy()
        print('copy: ', d_copy)
        d_copy.pop(i)
        print(d_copy)
        if is_ascending(d_copy) or is_descending(d_copy):
            for i, n in enumerate(d_copy):
                if i == 0:
                    safe = True
                elif (n != value) and (1 <= abs(n - value) <= 3):
                    safe = True
                else:
                    safe = False
                    break
                value = n
        #print(line, safe)
        if safe:
            sum += 1
            break
    return sum

for line in data:
    s = safe_check(line)
    sum += s

print(data)
    
print(sum)
