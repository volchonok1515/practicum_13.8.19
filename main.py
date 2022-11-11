ticket = int(input("Веедите количество билетов: "))
age_visitor = 0
price = 0
price_discount = 0
for visitor in range(ticket):
    age_visitor = int(input("Ввведите возраст: "))
    if age_visitor < 18:
        price = 0

    elif 18 <= age_visitor <= 25:
        price +=990

    else:
        price+= 1390

if ticket >= 3:
    price_discount = price * 0.9

print(price or price_discount)
