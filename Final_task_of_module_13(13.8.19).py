sum_all = 0
i = 1

tickets = input ("Сколько билетов вы хотите приобрести >\t")
tickets = int (tickets)

while i <= tickets:
    age = input(f"Для какого возраста покупается билет №{i}>\t")
    age = int(age)
    if age < 18:
        print("Билет бесплатный")
    elif 18 <= age < 25:
        sum_all += 990
        print ("Стоимость билета 990 рублей")
    elif age >= 25:
        sum_all += 1330
        print("Стоимость билета 1330 рублей")
    i=i+1

if tickets > 3:
        sum_all = sum_all - ((sum_all / 100) * 10)
        print ("Для вас действует скидка 10%")
        print ("Общая сумма к оплате, с учетом скидки >\t", sum_all,"руб.")
else:
    print ("Общая сумма к оплате >\t", sum_all,"руб.")