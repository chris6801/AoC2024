# Day 1, Part 1
with open('one.txt') as f:
    data = f.readlines()
    data_l = [int(item.strip().split('   ')[0]) for item in data]
    data_l.sort()
    data_r = [int(item.strip().split('   ')[1]) for item in data]
    data_r.sort()
    data = list(zip(data_l, data_r))
    
count = 0

for line in data:
    diff = abs(line[0] - line[1])
    count += diff
    
print(count)
