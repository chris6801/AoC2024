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
    
new_valids = 0
count = 0

invalids = []
    
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
        pass
    else:
        invalids.append(update)

# uses bubble sort algorithm to swap pages
# based on the rule list
for update in invalids:
    print('before: ', update)
    for i in range(len(update)):
        for j in range(0, len(update) - i - 1):
            for rule in rules:
                if update[j] == rule[0] and rule[1] in update:
                    j_idx = j
                    r_idx = update.index(rule[1])
                    if j_idx < r_idx:
                        update[j_idx], update[r_idx] = update[r_idx], update[j_idx]
                        
                        
    middle = (len(update) - 1) // 2
    new_valids += update[middle]
    count += 1
    print('after: ', update)

print(new_valids)