tickets_count = int(input('Введите количество билетов \n'))
age = [int(input('Введите возраст посетителя \n')) for i in range (tickets_count)]
cost = 0
for i in age:
    if i < 18:
        cost += 0
    if 18 <= i < 25:
        cost += 990
    if i >= 25:
        cost += 1390
if tickets_count > 3:
    cost *= 0.9
print(cost)