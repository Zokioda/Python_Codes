import random

numbers = []
odd = 0
even = 0
for i in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
for i in range(10):
    if numbers[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print("There are ", even, " even numbers")
print("There are ", odd, " odd numbers")
