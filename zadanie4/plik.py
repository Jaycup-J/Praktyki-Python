numbers = [2,1,5,3,6, 0, -29, 32, 124]

counter = 1

while counter != 0:
    counter = 0
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            counter += 1

print(numbers)