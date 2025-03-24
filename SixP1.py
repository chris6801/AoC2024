import console
import time
from copy import deepcopy

with open('six.txt') as f:
    data = f.readlines()
    data = [list(item.strip()) for item in data]

print(len(data))
    
initial_guard_pos = []

d_idx = 0
    
for i, line in enumerate(data):
    for j, char in enumerate(line):
        #print('line length: ', len(line))
        if char == '^' or char == '>' or char == 'v' or char == '<':
            initial_guard_pos = [i,j]
            #data[i][j] == 'X'
            if char == '^':
                d_idx = 0
            elif char == '>':
                d_idx = 1
            elif char == '<':
                d_idx = 2
            else:
                d_idx = 3
            print('init: ',char)
        #data_map[(j, i)] = char
        
data_map = data

guard_pos = initial_guard_pos
        
dxdy = [[-1, 0], [0, 1], [1, 0], [0, -1]]

in_map = True

prev_obs = []

def can_move(pos, dxdy, dmap, d_idx, prev_obs):
    dy = dxdy[d_idx][0]
    dx = dxdy[d_idx][1]
    target = pos[0] + dy, pos[1] + dx
    if 0 <= target[0] <= 129 and 0 <= target[1] <= 129:
        in_map = True
    else:
        in_map = False
    if in_map:
        if dmap[target[0]][target[1]] != '#':
            return True
        else:
            prev_obs.append([pos[0], pos[1], dxdy[d_idx]])
            return False
    elif not in_map:
        return True
    return False
        
def move(pos, dxdy, dmap, d_idx, prev_obs):
    dy = dxdy[d_idx][0]
    dx = dxdy[d_idx][1]
    new_pos = [pos[0] + dy, pos[1] + dx]
    dmap[pos[0]][pos[1]] = 'X'
    print(f"Marked X at position {pos}")
    return new_pos

def display(guard_pos, data_map):
    console.clear()
    
    # Display a 6x5 area around the guard position
    print(
        data_map[guard_pos[0]-2][guard_pos[1]-2],
        data_map[guard_pos[0]-2][guard_pos[1]-1],
        data_map[guard_pos[0]-2][guard_pos[1]],
        data_map[guard_pos[0]-2][guard_pos[1]+1],
        data_map[guard_pos[0]-2][guard_pos[1]+2],
        data_map[guard_pos[0]-2][guard_pos[1]+3]
    )
    print(
        data_map[guard_pos[0]-1][guard_pos[1]-2],
        data_map[guard_pos[0]-1][guard_pos[1]-1],
        data_map[guard_pos[0]-1][guard_pos[1]],
        data_map[guard_pos[0]-1][guard_pos[1]+1],
        data_map[guard_pos[0]-1][guard_pos[1]+2],
        data_map[guard_pos[0]-1][guard_pos[1]+3]
    )
    print(
        data_map[guard_pos[0]][guard_pos[1]-2],
        data_map[guard_pos[0]][guard_pos[1]-1],
        '*',  # Current position
        data_map[guard_pos[0]][guard_pos[1]+1],
        data_map[guard_pos[0]][guard_pos[1]+2],
        data_map[guard_pos[0]][guard_pos[1]+3]
    )
    print(
        data_map[guard_pos[0]+1][guard_pos[1]-2],
        data_map[guard_pos[0]+1][guard_pos[1]-1],
        data_map[guard_pos[0]+1][guard_pos[1]],
        data_map[guard_pos[0]+1][guard_pos[1]+1],
        data_map[guard_pos[0]+1][guard_pos[1]+2],
        data_map[guard_pos[0]+1][guard_pos[1]+3]
    )
    print(
        data_map[guard_pos[0]+2][guard_pos[1]-2],
        data_map[guard_pos[0]+2][guard_pos[1]-1],
        data_map[guard_pos[0]+2][guard_pos[1]],
        data_map[guard_pos[0]+2][guard_pos[1]+1],
        data_map[guard_pos[0]+2][guard_pos[1]+2],
        data_map[guard_pos[0]+2][guard_pos[1]+3]
    )

    print('position: ', guard_pos)
    
    time.sleep(0.005)
    
total = 0
    
def test_path(dmap, guard_pos, dxdy, d_idx, prev_obs):
    working_map = dmap    
    while True:
        c_move = can_move(guard_pos, dxdy, dmap, d_idx, prev_obs)
        if not (0 <= guard_pos[0] <= 129 and 0 <= guard_pos[1] <= 129):
            print(f"Path complete - checking map")
            for row in working_map:
                if 'X' in row:
                    print("Found X in map")
            return dmap, 0
        #display(guard_pos, data_map)
        print(guard_pos)
        if [guard_pos[0], guard_pos[1], dxdy[d_idx]] in prev_obs:
            print("Loop detected")
            return dmap, 1
        if c_move:
            #data_map[guard_pos[0]][guard_pos[1]] = 'X'
            guard_pos = move(guard_pos, dxdy, dmap, d_idx, prev_obs)
        else:
            d_idx = (d_idx + 1) % len(dxdy)

data_map, result = test_path(data_map, guard_pos, dxdy, d_idx, prev_obs)

print(data_map)

possible_obs = []
        
for i, line in enumerate(data_map):
    for j, char in enumerate(line):
        if char == 'X':
            possible_obs.append([i, j])
            
print('obs: ', possible_obs)
            
'''for obs in possible_obs:
    test = deepcopy(data_map)
    test[obs[0]][obs[1]] = '#'
    guard_pos = initial_guard_pos
    d_idx = 0
    val = test_path(test, guard_pos, dxdy, d_idx)
    if val == 1:
        total += 1'''
    
print(total)