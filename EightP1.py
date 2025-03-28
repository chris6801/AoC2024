from itertools import combinations

with open('eight.txt') as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    
locs = {}
for i, line in enumerate(data):
    for j in range(len(line)):
        if data[i][j] != '.':
            if data[i][j] in locs.keys():
                locs[data[i][j]].append([i,j])
            else:
                locs[data[i][j]] = [[i,j]]
                
total = 0

print(len(data[0]))
used = []
for loc in locs.values():
    combs = list(combinations(loc, 2))
    for comb in combs:
        comby0, combx0 = comb[0]
        comby1, combx1 = comb[1]
        delta = [comby0 - comby1, combx0 - combx1]
        print(delta)
        if 0 <= comby0 + delta[0] <= len(data) - 1 and 0 <= combx0 + delta[1] <= len(data[0]) - 1 and [comby0 + delta[0], combx0 + delta[1]] not in used:
            used.append([comby0 + delta[0], combx0 + delta[1]])
            total += 1
        if 0 <= comby1 + -delta[0] <= len(data) - 1 and 0 <= combx1 + -delta[1] <= len(data[0]) - 1 and [comby1 + -delta[0], combx1 + -delta[1]] not in used:
            used.append([comby1 + -delta[0], combx1 + - delta[1]])
            total += 1
            
print(total)
            
