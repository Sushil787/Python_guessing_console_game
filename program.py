
import random
from datetime import date
score = 0
times = 0
name = input("\tenter your name: ")
age  = int(input("\tinput the age: "))
print(f"\t{name} Welcome to guessing game")
print("____________________________________________________________________________________________________")

while (True):
    for i in range(1, 7):
        print(f" Name = {name}     Age = {age}                                         Today's Date",date.today())

        print("____________________________________________________________________________________________________")

        i = int(input("input the no: "))

        r = random.randint(1, 3)
        if (i == r):
            score += 1
            print("_______")
            print("|good!!|")
            print("|______|")
        else:
            times += 1
            if (i < r):
                print("its less")
            else:
                print("high")

    if (times > 3):
        print(f"\n{name} it's satisfactory, you did it by scoring {score} ,with {times} negative marking")
        status = input(f"{name} do you want to continue if so, yes/no: ")
        if (status == "yes"):
            break

        else:
            continue

    elif (times == 0):
        print("{name}, you loose ...Try again ")
        status = input(f"{name} do you want to continue if so, yes/no: ")
        if(status == "yes"):
            continue
        else:
            break

    else:
        print(f"\n{name} good you did it by scoring {score} with {times} negative marking")
        status = input("{name} do you want to continue if so, yes/no: ")
        if (status == "yes"):
            break
        else:
            continue
