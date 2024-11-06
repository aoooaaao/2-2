def t0():
    print("Введите номер задачи: ")
    n=int(input())
    if n==1:
        import task1
    elif n==2:
        import task2
    elif n==3:
        import task3
    elif n==4:
        import task4
    elif n == 5:
        import task5
    elif n == 6:
        import task6
    elif n == 7:
        import task7
    elif n == 8:
        import task8
    elif n == 9:
        import task9
    elif n == 10:
        import task10
    elif n > 10:
        print("Такой задачи не существует")
while True:
    t0()
    x = str(input("Введите q, чтобы выйти: "))
    if x == 'q':
        continue
    else:
        break