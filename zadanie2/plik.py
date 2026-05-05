list = [3, -6, 2, -5, 12]

max = 0

for element in list:
    if element > max:
        max = element

min = max

for element in list:
    if element < min:
        min = element

print(max)
print(min)