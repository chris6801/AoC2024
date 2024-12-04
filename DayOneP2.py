# Day 1, Part 2
with open('one.txt') as f:
    data = f.readlines()
    data_l = [int(item.strip().split('   ')[0]) for item in data]
    data_l.sort()
    data_r = [int(item.strip().split('   ')[1]) for item in data]
    data_r.sort()
    data = list(zip(data_l, data_r))
    
sum = 0

for line in data:
    l = line[0]
    if l in data_r:
        num = l
        num *= data_r.count(l)
        print(num)
        sum += num
        
print(sum)
