food = input("укажи затраты на еду: ")
transport = input("укажи затраты на транспорт: ")
entertainment = input("укажи затраты на развлечения: ")

food = float(food)
transport = float(transport)
entertainment = float(entertainment)

sum = food + transport + entertainment
average = sum / 3

print(f"общие затраты: {sum}")
print(f"средние траты: {average}")