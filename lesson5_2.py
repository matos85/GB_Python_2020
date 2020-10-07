j = 0
lst = []
ii = 1
with open('for_dz_2.txt', 'r', encoding='utf-8')as f:
    for line in f:
        print(line.strip())
        print(f'Количество слов: {len(line.split())}\n')
        lst.append(line.strip())
        j += 1

print(f'Количество строк: {j}')

