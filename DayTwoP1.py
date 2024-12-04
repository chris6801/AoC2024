with open('two.txt') as f:
    data = f.readlines()
    data = [item.strip().split(' ') for item in data]
    data = list(map(lambda x: list(map(int, x)), data))

sum = 0

def is_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    
def is_descending(lst):
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

for line in data:
    value = None
    safe = False
    if is_ascending(line) or is_descending(line):
        for i, n in enumerate(line):
            if i == 0:
                safe = True
                pass
            elif (n != value) and (1 <= abs(n - value) <= 3):
                safe = True
            else:
                safe = False
                break
            value = n
    print(line, safe)
    if safe:
        sum += 1
        
print('descending: ',is_descending(([3,2,1])))
print(sum)
