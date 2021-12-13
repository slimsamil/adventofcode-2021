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

one_list = []
zero_list = []

for i in range(0, 12):
    for x in content:
        if x[i] == '1':
            one += 1
            one_list.append(x)
        else:
            zero += 1
            zero_list.append(xç)
        
    if one > zero:
        content = one_list
    else:
        content = zero_list
    
    one = 0
    zero = 0
    ne_list = []
    zero_list = []

print(content)





        