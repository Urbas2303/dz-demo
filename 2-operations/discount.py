price = input("укажи цену товара: ")
discount_percent = input("укажи скидку: ")

price = float(price)
discount_percent = float(discount_percent)

discount = price / 100 * discount_percent
price -= discount

print(f"цена со скидкой: {price}")
