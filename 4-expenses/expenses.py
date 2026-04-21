# expense = input("Введи сумму: ")

# if not 'руб' in expense:
#     print("Некорректный формат суммы")
#     exit()

# rub, kop = expense.lower().split("руб")

# try:
#     rub = float(rub.strip())
# except ValueError:
#     print("Некорректный формат суммы")
#     exit()

# if len(kop) != 0 and kop.endswith("коп"):
#     try:
#         kop = float(kop.replace("коп", "").strip()) / 100
#     except ValueError:
#         print("Некорректный формат суммы")
#         exit()
# else:
#     kop = 0

# result = rub + kop

# print(f"{result:.2f} ₽")

while True:
    print("===Меню===")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать сумму и средний расход")
    print("4. Удалить расход по номеру")
    print("5. Выход")
    print("_" * 30)

    try:
        choose = int(input("Выбери пункт меню: "))
    except ValueError:
        print("Некорректный ввод")
        continue

    if choose == 5:
        break
