with open('five.txt') as f:
    data = f.readlines()
    data = [item.strip() for item in data]
    rules = []
    updates = []
    tripped = False
    for line in data:
        if line != '' and not tripped:
            rules.append(line)
        elif line == '':
            tripped = True
        else:
            updates.append(line)
    rules = [rule.split('|') for rule in rules]
    rules = list(map(lambda x: list(map(int, x)), rules))
    updates = [update.split(',') for update in updates]
    updates = list(map(lambda  x: list(map(int, x)), updates))
    
valids = 0
count = 0
    
for update in updates:
    valid = False
    for page in update:
        for rule in rules:
            if page == rule[0] and rule[1] in update:
                if update.index(page) < update.index(rule[1]):
                    valid = True
                else:
                    valid = False
                    break
        if not valid:
            break
    if valid:
        print('update: ', update)
        print('length: ', len(update))
        middle = (len(update) - 1) // 2
        valids += update[middle]
        count += 1
        print('middle idx: ', middle)
        print('value: ', update[middle])

print(len(updates))
print(count)
print(valids)