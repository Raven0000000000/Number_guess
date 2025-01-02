import random
zagadannoe_chislo = random.randint(1,10)
print(zagadannoe_chislo)
i = 1
while True:
    if i <= 3:
        vvod = int(input(f"Какое число я загадал?\nПопытка {i}:"))
        if vvod > zagadannoe_chislo:
            print("Я загадал число по меньше.")
            i +=1
        elif vvod < zagadannoe_chislo:
            print ("Я загадал число поболше.")
            i += 1
        else:
            print("Ты угадал - МОЛОДЕЦ!")
            break
    else:
        print ("У тебя закончились попытки!")
        break