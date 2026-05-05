numbers = [1, 2, 39, 18, 4, 5, 16, 7]

suma = int(input("Podaj liczbę L \n"))

stop = False

for index, number in enumerate(numbers):
    for i in range(len(numbers)):
        if number + numbers[i] == suma and i != index:
            print("Tak, sumę tę dają liczby " + str(number) + " i " + str(numbers[i]))
            stop = True
            break
    if stop:
        break