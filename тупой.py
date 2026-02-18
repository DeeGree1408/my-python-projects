name = input("Привет! Как тебя зовут? ")
while name == "":
    name = input("Ещё раз: Как тебя зовут? ")
city = input("В каком городе ты живёшь? ")
while city == "":
    city = input("Ещё раз: В каком городе ты живёшь? ")
number = input("Какое твоё любимое число? ")
while number == "" or number.isdigit() == False:   
    number = input("Введи, пожалуйста, положительное число ")
number = int(number)
print(f"Привет, {name}, из города {city}!")
print(f"Твоё любимое число - {number}")
print(f"А если его умножить на 2, будет {number*2}")
print(f"Кто молодец? {name} - МОЛОДЕЦ!!!")