def puti():
    vib = input("Выберете путь:\n1.Лес\n2.Поле\n3.Город\nВвод:")
    if vib == "1":
        print(1)
    elif vib == "2":
        print(2)
    elif vib == "3":
        print(3)
    else:
        print("Введите число из указанного списка")
        puti()