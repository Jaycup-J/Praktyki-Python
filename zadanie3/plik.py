string = input("Podaj string do sprawdzenia \n")

responses = [input("Zliczyc wyrazy? (tak lub nie) \n"), input("Zliczyc litery? (tak lub nie) \n"), input("Zbadac czestotliwosc liter? (tak lub nie) \n")]

alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźżqvxAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻQVX"

if responses[0] == "tak":
    print(len(string.split(" ")))
if responses[1] == "tak":
    counter = 0
    for char in string:
        if char in alphabet:
            counter += 1
    print(counter)
if responses[2] == "tak":
    letters = []
    frequencies = []
    for char in string:
        if char in alphabet:
            counter = 0
            for index, letter in enumerate(letters):
                if char == letter:
                    frequencies[index] += 1
                    counter += 1
                    break
            if counter == 0:
                letters.append(char)
                frequencies.append(1)
    for i in range(len(letters)):
        print(str(letters[i]) + " - " + str(frequencies[i]))
        
                    