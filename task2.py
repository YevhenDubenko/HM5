import random

first_my_list = []
second_my_list = []
results = []
i = 1

while i <= 10:
    first_my_list.append(random.randint(1, 10))
    second_my_list.append(random.randint(1, 10))
    i += 1
print(first_my_list)
print(second_my_list)

for element in first_my_list:
    if element in second_my_list:
        results.append(element)
print(results)
