print(f"Привет! Ответь на три вопроса!")
name = input("Как тебя зовут?")
while name == "":
    name = input("Ты не ответил на вопрос... Как тебя зовут? ")
    while name == "":
        name = input("Снова пусто! Как тебя зовут? ")
age = input("Сколько тебе лет? ")
while age.isdigit() == False:
    age = input("Ты ввёл текст, Введи цифровое значение! ")
color = input("Какой твой любимый цвет? ")
print(f"Спасибо! Вот что ты рассказал:")    
print(f"Тебя зовут {name}.")
print(f"Тебе {age} лет.")
print(f"Твой любимый цвет {color}.")