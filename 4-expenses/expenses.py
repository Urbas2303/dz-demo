def parse_expense(expense_str: str) -> tuple[float | None, str | None]:
    if not 'руб' in expense_str:
        return None, "Некорректный формат суммы"

    rub, kop = expense_str.lower().split("руб")

    try:
        rub = float(rub.strip())
    except ValueError:
        return None, "Некорректный формат суммы"

    if len(kop) != 0 and kop.endswith("коп"):
        try:
            kop = float(kop.replace("коп", "").strip()) / 100
        except ValueError:
            return None, "Некорректный формат суммы"
    else:
        kop = 0

    result = rub + kop

    return result, None


def add_expense(expenses: list[float], value: float) -> list[float]:
    expenses.append(value)
    return expenses


def choose_menu_add_expense(expenses: list[float]):
    expense_str = input("Введи сумму в формате {[сумма] руб [сумма] коп}\n")
    expense, err = parse_expense(expense_str)
    if not err is None:
        print(err)
        return

    if not expense is None:
        add_expense(expenses, expense)
        return

    print("Что-то пошло не так, попробуйте снова")


def print_report(expenses: list[float]):
    print("===Список всех расходов===")
    for index, expense in enumerate(expenses):
        print(f"[{index + 1}. {expense}]")
    print("_" * 30)


def get_total(expenses: list[float]) -> float:
    return sum(expenses)


def get_average(expenses: list[float]) -> float:
    return sum(expenses) / len(expenses)


def delete_expense(expenses: list[float], index: int):
    del expenses[index]


def choose_menu_get_total_average(expenses: list[float]):
    total = get_total(expenses)
    average = get_average(expenses)

    print(f"Сумма: {total}")
    print(f"Среднее: {average}")
    print("_" * 30)


def choose_menu_delete_expense(expenses: list[float]):
    number = input("Какой расход вы хотите удалить: ")
    try:
        number = int(number)
    except ValueError:
        print("Некорректный номер")
        return
    if number <= 0 or number > len(expenses):
        print("Некорректный номер")
        return
    delete_expense(expenses, number - 1)
    print("Успешно")


expenses: list[float] = []

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

    match choose:
        case 1:
            choose_menu_add_expense(expenses)
        case 2:
            print_report(expenses)
        case 3:
            choose_menu_get_total_average(expenses)
        case 4:
            choose_menu_delete_expense(expenses)
        case 5:
            exit()
        case _:
            print("Некорректный ввод")
            continue
