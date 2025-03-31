from itertools import combinations
import numpy as np
import math

with open('eight.txt') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

print(repr(data))

h = len(data)
w = len(data[0])

h_w = (h, w)

print(h_w)

locs = {}
for i, line in enumerate(data):
    for j in range(len(line)):
        if data[i][j] != '.':
            if data[i][j] in locs.keys():
                locs[data[i][j]].append(np.array([i,j]))
            else:
                locs[data[i][j]] = [np.array([i,j])]
                
total = 0

def in_bounds(coords, map_h_w):
    return 0 <= coords[0] < map_h_w[0] and 0 <= coords[1] < map_h_w[1]

print(len(data[0]))
used = []
for loc in locs.values():
    print('locations: ', loc)
    combs = list(combinations(loc, 2))
    for comb in combs:
        print(comb)
        comby0, combx0 = comb[0]
        comby1, combx1 = comb[1]
        delta_y = comby0 - comby1
        delta_x = combx0 - combx1
        
        gcd = math.gcd(abs(delta_y), abs(delta_x))
        
        delta = np.array([delta_y // gcd, delta_x // gcd])
        
        target = comb[0]
        print(delta)
        i = 0
        while in_bounds((i * delta) + target, h_w):
            print('loop1')
            current_point = (i * delta) + target
            if len(used) == 0 or not any(np.array_equal(current_point, u) for u in used):
                used.append(current_point)
                total += 1
            i += 1
        target = comb[1]
        i = 0
        while in_bounds(-(i * delta) + target, h_w):
            print('loop2')
            current_point = -(i * delta) + target
            if len(used) == 0 or not any(np.array_equal(current_point, u) for u in used):
                used.append(current_point)
                total += 1
            i += 1
        
    if len(combs) > 1:
        for l in loc:
            if not any(np.array_equal(l, u) for u in used):
        
                total += 1
            
print('total:', total)
print(data)
            