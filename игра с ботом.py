b_w = 0
c_w = 0
for i in range(2000):
    import random
    list = [1, 2, 3, 4, 5, 6]
    b = random. choice(list)
    c = random. choice(list)
    if "Да" == "Да":
        print("Тебе выпало: " + str(b))
        print("Боту выпало: " + str(c))
    if b > c:
        b_w += 1
        print("Победил ты")
    elif b < c:
        c_w += 1
        print("Победил бот")

    elif c == b:
        b_w += 1
        c_w += 1
        print("Ничья")
    elif a == "Нет":

        print("Отмененно.")
    else:

        print("Ошибка!")
print("Ты " + str(b_w))
print("Комп " + str(c_w))
