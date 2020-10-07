staffer, employees, all_employees = [], [], []

with open('for_dz_3.txt', 'r', encoding='utf-8') as f:
    for i in f:
        staffer.append(i.strip())

print('Cотрудник с з/п меньше 20К:')
for j in staffer:
    k = j.strip()
    for w in k.split(':'):
        if w.isdigit():
            all_employees.append(int(':'.join(k.split(':')[-1:])))
        if w.isdigit() and int(w) < 20000:
            print(':'.join(k.split(':')[:-1]))
            employees.append(int(':'.join(k.split(':')[-1:])))
print(f'Cредняя величина дохода сотрудников с з/п меньше 20К: {int(sum(employees) / len(employees))}')
print(f'Cредняя величина дохода сотрудников: {int(sum(all_employees) / len(all_employees))}')
