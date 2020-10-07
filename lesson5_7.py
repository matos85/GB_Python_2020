import json

company = []
profit = {}
avrg_profit = {}
a = []
total = []
with open('for_dz_7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        company.append(line.strip().split())
for i in company:  #
    z = i[0]
    s = int(i[-2]) - int(i[-1])
    profit[z] = s
    if s < 0:
        s = 0
    a.append(s)
    avrg_profit['average_profit'] = sum(a)

total.append(profit)
total.append(avrg_profit)
print(total)

with open('jsonf.json', 'w') as f:
    json.dump(total, f)
