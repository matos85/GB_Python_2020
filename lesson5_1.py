i = input('введите текст через пробел: ').split()
with open('for_dz_1.txt', 'w+', encoding='utf-8')as f:
    for j in i:
        f.writelines(j+'\n')
