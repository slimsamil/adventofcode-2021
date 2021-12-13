data = open('day1/day1.txt', 'r')

content = data.read().split('\n')

print(content)

print(len(content))

i = 0

    
for x in range(len(content)-3):
    if ((int(content[x])+int(content[x+1])+int(content[x+2])) < (int(content[x+1])+int(content[x+2])+int(content[x+3]))):
        i += 1
        
print(i)
