from itertools import product
import operator

ops = [operator.add, operator.mul]

def generate_set(lst, size):
    return [list(p) for p in product(lst, repeat=size)]

with open('seven.txt') as f:
    data = f.readlines()
    data = [item.strip().split(': ') for item in data]
    result = []
    for line in data:
        sub = []
        for item in line:
            if ' ' in item:
                sub.extend(map(int, item.split()))
            else:
                sub.append(int(item))
            print('sub', sub)
        result.append(sub)
        
data = result
print(data)

total = 0
list_sizes = []
master = {}

for line in data:
    if (len(line)-1) not in master.keys():
        ops_list = generate_set(ops, len(line)-1)
        master[len(line)-1] = ops_list
    else:
        ops_list = master[len(line)-1]
    print(master)
    solution = line[0]
    for ops in ops_list:
        broke = False
        for op in ops:
            curr = line[1]
            for i in range(1, len(line)-1):
                curr = op(curr, line[i+1])
            if curr == solution:
                total += solution
                broke = True
                break
        if broke:
            break

print(total)