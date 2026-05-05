import time
import random
points = 0
botpoints = 0
while True:
    choice = input("Orzeł (o) czy reszka (r)? \n")
    if choice == "0":
        break
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    randnum = random.randint(1, 2)
    if randnum == 1:
        print("ORZEŁ!")
        if choice == "r":
            botpoints += 1
        else:
            points += 1
    else:
        print("RESZKA!")
        if choice == "r":
            points += 1
        else:
            botpoints += 1
    print("Gracz: " + str(points))
    print("Bot: " + str(botpoints))