expense = input("Введи сумму: ")

if not 'руб' in expense:
    print("Некорректный формат суммы")
    exit()

rub, kop = expense.split("руб")

rub = float(rub.strip())

if len(kop) != 0 and kop.endswith("коп"):
    kop = float(kop.replace("коп", "").strip()) / 100
else:
    kop = 0

result = rub + kop

print(f"{result:.2f} ₽")
