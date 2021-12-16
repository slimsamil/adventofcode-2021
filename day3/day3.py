data = open('day3/day3.txt', 'r')

content = data.read().split('\n')

#########PART 1########
one = 0
zero = 0
gamma = ""
epsilon = ""

for i in range(0, 12):
    for x in content:

        if x[i] == '1':
            one += 1
        else:
            zero += 1

    if one > zero :
        gamma += "1"
        epsilon += "0"
    
    else: 
        gamma += "0"
        epsilon += "1"

    one = 0
    zero = 0

print(int(gamma, 2) * int(epsilon, 2))

#######PART 2#########
content1 = content.copy()
one_list = []
zero_list = []

for i in range(0, len(content1[0])):
    for x in content1:
        if x[i] == '1':
            one += 1
            one_list.append(x)
        else:
            zero += 1
            zero_list.append(x)
    if zero > one:
        content1 = zero_list
    else: 
        content1 = one_list
    
    one = 0
    zero = 0
    one_list = []
    zero_list = []

print(content1)

content2 = content.copy()

for i in range(0, 12):
    for x in content2:
        if x[i] == '1':
            one += 1
            one_list.append(x)
        else:
            zero += 1
            zero_list.append(x)

    if(len(content2) > 1):
        if one < zero:
            content2 = one_list
        else:
            content2 = zero_list

    one = 0
    zero = 0
    one_list = []
    zero_list = []

print(content2)
number1 = int(content1[0], 2)
number2 = int(content2[0], 2)
print(number1)
print(number2)

print(number1*number2)





        
