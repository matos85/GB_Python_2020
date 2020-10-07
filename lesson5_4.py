z = []
with open('for_dz_4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        strk = line.strip().split()
        if strk[-1] == '1':
            strk[0] = 'Один'
            z.append(strk)
        if strk[-1] == '2':
            strk[0] = 'Два'
            z.append(strk)
        if strk[-1] == '3':
            strk[0] = 'Три'
            z.append(strk)
        if strk[-1] == '4':
            strk[0] = 'Четыре'
            z.append(strk)
print(z)

with open('for_dz_4.1.txt', 'w', encoding='utf-8') as f:
    for i in z:
        i=(' '.join(i))
        f.write(i)
        f.write('\n')


# print(':'.join(line.split(':')[:-1]))
