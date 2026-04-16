expense = input("Введи сумму: ")

if not 'руб' in expense:
    print("Некорректный формат суммы")
    exit()

rub, kop = expense.lower().split("руб")

try:
    rub = float(rub.strip())
except ValueError:
    print("Некорректный формат суммы")
    exit()

if len(kop) != 0 and kop.endswith("коп"):
    try:
        kop = float(kop.replace("коп", "").strip()) / 100
    except ValueError:
        print("Некорректный формат суммы")
        exit()
else:
    kop = 0

result = rub + kop

print(f"{result:.2f} ₽")
