print(f"Привет! Ответь на три вопроса!")
name = input("Как тебя зовут?")
while name == "":
    name = input("Ты не ответил на вопрос... Как тебя зовут? ")
    while name == "":
        name = input("Снова пусто! Как тебя зовут? ")
age = input("Сколько тебе лет? ")
while age.isdigit() == False:
    age = input("Ты ввёл текст, Введи цифровое значение! ")
age = int(age)
if age > 120:
    print("Ты дебил")
    else 
color = input("Какой твой любимый цвет? ")
while color == "":
    color = input("Ты не указал цвет! ")
print(f"Спасибо! Вот что ты рассказал:")    
print(f"Тебя зовут {name}.")
print(f"Тебе {age} лет. Через 10 лет тебе будет {age + 10} лет")
print(f"Твой любимый цвет {color}.")