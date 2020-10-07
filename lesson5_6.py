my_dict = {}
num_list = []
num = ''
full=[]
haff=[]
with open('for_dz_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        i = line.find(':')
        if i != -1:
            my_dict[line[:i]] = 0
            haff.append(line[:i])
            a = line[i + 2:]
            for char in a:
                if char.isdigit():
                    num = num + char
                else:
                    if num != '':
                        num_list.append(int(num))
                        num = ''
            if num != '':
                num_list.append(int(num))
        full.append(sum(num_list))
        num_list=[]
for k,j in my_dict.items():
    k=full[j]
for y in range(len(haff)):
    my_dict[haff[y]]=full[y]
print(my_dict)


