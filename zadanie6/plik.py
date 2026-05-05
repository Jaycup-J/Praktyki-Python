num = int(input("Podaj szukaną liczbę \n"))

numbers = list(range(1, 1000))
tempnumbers = []
iteration = 1

print(numbers)

found = False
idx = 0

while not found:
    if len(numbers) % 2 != 0:
        midex = int((len(numbers) - 1) / 2)
    else:
        midex = int(len(numbers) / 2) #prawy

    if midex == 0 and not numbers:
        print("Liczby nie ma w tablicy")
        found = True

    if not found:
        if numbers[midex] == num:
            print("Liczba znajduje się w tablicy na indeksie " + str(midex + idx))
            found = True
        else:
            if len(numbers) == 1:
                print("Liczby nie ma w tablicy")
                found = True
            if num < numbers[midex]:
                for i in range(midex):
                    tempnumbers.append(numbers[i])
                numbers = tempnumbers.copy()
                tempnumbers = []
            else:
                for i in range(midex + 1, len(numbers)):
                    tempnumbers.append(numbers[i]) 
                idx += len(numbers) - len(tempnumbers)
                numbers = tempnumbers.copy()
                tempnumbers = []
    print("Iteracja " + str(iteration) + ": ")
    print(numbers)
    iteration += 1