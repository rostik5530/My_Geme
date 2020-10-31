from STATS import *
def Start():
    def name(NAME):
        test = input("Вы ввели имя:" + NAME + " Вы уверены что хотите это имя(Y,N)")
        if test == "Y" or test == "y":
            print("Тогда добро пожаловать в мир страхов и ужасов")
            ststs.update({1: NAME})
            return ststs
        else:
            NAME = input("Введите имя:")
            name(NAME)

    print("Добро пожаловать в Игру)))")
    NAME = input("Введите имя:")
    return name(NAME)
