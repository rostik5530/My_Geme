from STATS import *
from puti import *


def menu():
    HP = ststs[2]
    proschet()
    put = input("Меню выберите пункт:\n1.выбрать дорогу\n2.отдохнуть\n3.статистика\n4.перезапуск игры\n"
                "5.читы\nВвод:")
    if put == "1":
        puti()
        menu()
    if put == "2":
        if HP < MAX_HP - 10:
            HP += 10
            print("Вы подлечились")
            menu()
        elif HP < MAX_HP:
            HP = MAX_HP
            print("Теперь у вас полные ХП")
            menu()
        else:
            print("Ваши HP полны")
            menu()
    if put == "3":
        print("Ваша статистика:\n" + ststs)
