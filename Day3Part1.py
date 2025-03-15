import re

text = "amul(512,20)"

with open('three.txt') as f:
    data = f.readlines()
    data = [line.strip() for line in data]
 
a = re.findall(r"mul\((\d+,\d+)\)", text)

print('match: ',a)

sum = 0

for line in data:
    matches = re.findall(r"mul\((\d+,\d+)\)", line)
    print('mul matches: ', matches)
    matches = [match.split(',') for match in matches]
    matches = list(map(lambda x: list(map(int, x)), matches)) 
    for match in matches:
        s = match[0] * match[1]
        sum += s

print(sum)
