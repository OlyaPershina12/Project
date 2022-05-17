import random


def exercise(selection):
    words_dict = {
        "malicious": "злобный",
        "majestic": "величественный",
        "nasty": "противный",
        "sorrowful": "печальный",
        "sullen": "угрюмый",
        "fortunate": "удачливый",
        "soothed": "успокоенный",
        "jealous": "завистливый",
        "stylish": "стильный",
        "perky": "весёлый",
        "gratified": "удовлетворённый",
        "resourceful": "изобретательный",
        "tedious": "нудный",
        "choosy": "привередливый",
        "peculiar": "странный",
        "proficient": "умелый",
        "immortal": "бессмертный",
        "gregarious": "общительный",
        "outgoing": "дружелюбный",
        "alarmed": "встревоженный",
        "adventurous": "предприимчивый",
    }
    amount = int(
        input(
            "Напишите нужное Вам количество слов для тренировки. Всего в словаре 21 слово! "
        )
    )
    while amount > len(words_dict):
        amount = int(
            input(
                "Введенное Вами число больше количества слов в словаре! Напишите снова нужное Вам количество слов для "
                "тренировки. Всего в словаре 21 слово! "
            )
        )
    done_correctly = 0
    print('Если хотите завершить упражение досрочно введите "stop"')
    keys = list(words_dict.keys())
    values = list(words_dict.values())
    mix = list(zip(keys, values))
    random.shuffle(mix)
    words, meanings = zip(*mix)
    for i in range(amount):
        a = ""
        if selection == "1":
            print(words[i])
            a = meanings[i]
        elif selection == "2":
            print(meanings[i])
            a = words[i]
        translation = input("Введите перевод данного слова: ").lower().strip()
        if translation == a:
            done_correctly += 1
            print("Молодец, верно :)")
        elif translation == "stop":
            break
        else:
            print("К сожалению данный перевод неверен :(")
    print("Вы правильно ответили", done_correctly, "раз(а) из", amount)


while True:
    select_exercise = (
        input(
            'Выберите номер задания, которое Вы бы хотели выполнить. Данная программа имеет два типа '
            'заданий:\n1 - на экран будет выведено слово на английском языке и Вам нужно дать '
            'перевод данного слова на русском языке.\n2 - Вам будет дан перевод слова и его '
            'нужно будет написать на английском языке.\nДля выполнения заданий Вам следует ввести 1 или '
            '2. Если Вы захотите выйти из программы напишите "enough": '
        )
        .lower()
        .strip()
    )

    if select_exercise == "1" or select_exercise == "2":
        exercise(select_exercise)
    elif select_exercise == "enough":
        print("Вы вышли из программы!")
        break
    else:
        print("Вы ввели число отличное от 1 или 2!")
