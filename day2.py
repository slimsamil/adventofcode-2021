data = open('day2.txt', 'r')

content = data.read().split('\n')

print(content)

print(len(content))

forward = 0
aim = 0
depth = 0

for x in content:
    if x.startswith('forward'):
        forward += int(x[-1:])
        depth += int(x[-1:]) * aim
    elif x.startswith('down'):
        aim += int(x[-1:])
    elif x.startswith('up'):
        aim -= int(x[-1:])
        
    
                     
print(forward * depth)


1765720035
1181700834393
