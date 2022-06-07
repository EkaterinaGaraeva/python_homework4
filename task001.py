# Создать и заполнить файл случайными целыми значениями. 
# Выполнить сортировку содержимого файла по возрастанию.

import random

with open ('file.txt', 'w') as data:
    count = random.randint(2, 10)
    for i in range(0, count):
        data.write(str(random.randint(0, 100)) + '\n')


# def sorting_file_contents(file_with_numbers):
#     with open(file_with_numbers, 'r') as numbers:
#         numbers_from_file = numbers.read()
#         print(numbers_from_file)
#         numbers_from_file = sorted(numbers_from_file.split())
#         numbers_from_file = str(numbers_from_file)
#         numbers_from_file = numbers_from_file.replace("'", "")
#         numbers_from_file = numbers_from_file.replace("[", "")
#         numbers_from_file = numbers_from_file.replace("]", "")
#         numbers_from_file = numbers_from_file.replace(",", "")
#     return numbers_from_file

def sorting_file_contents(file_with_numbers):
    with open(file_with_numbers, 'r') as numbers:
        numbers_from_file = numbers.read().splitlines()
    numbers_from_file = list(map(int, numbers_from_file))
    print(numbers_from_file)
    numbers_from_file.sort()
    print(numbers_from_file)
    string_of_numbers = ''
    for j in numbers_from_file:
        string_of_numbers += str(j) + "\n"
    return string_of_numbers
    
with open ('file.txt', 'a') as data:
    data.write('\n' + 'Sorted numbers' + '\n' + sorting_file_contents('file.txt'))

#print(f"Отсортированные числа {sorting_file_contents('file.txt')}")

