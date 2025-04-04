with open('nine.txt') as f:
    new = []
    id = 0
    data = f.read()
    data = list(map(int, data.strip()))
    for i in range(0, len(data), 2):
        #print('i: ', i)
        for j in range(data[i]):
            new.append(id)
        id += 1
        if i < len(data) - 1:
            for k in range(data[i+1]):
                new.append('.')
                
a = new
                
right = []
idx = len(a) - 1
used = []
while idx >= 0:
    if a[idx] != '.' and a[idx] not in used:
        used.append(a[idx])
        curr = a[idx]
        next = a[idx]
        while next == curr:
            curr = a[idx]
            right.append(a[idx])
            idx -= 1
            next = a[idx]
        #print(right)
        for i in range(idx):
            if a[i] == '.':
                can_swap = True
                for j in range(1, len(right)):
                    if a[i+j] != '.':
                        can_swap = False
                        break
                if can_swap:
                    for k in range(len(right)):
                        a[i+k], a[idx+k+1] = right[k], '.'
                    right = []
                    break
        right = []
    else:
        idx -= 1
#print(a)

data = a

total = 0

for i in range(len(data)):
    if data[i] != '.':
        total += i * data[i]
        
print(total)