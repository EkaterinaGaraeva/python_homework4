# Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность 
# и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

def find_sequence(list_of_numbers, index, count):
    sequence = []
    sequence.append(list_of_numbers[index])
    j = index
    for i in range(j + count, len(list_of_numbers)):
        if list_of_numbers[i] > list_of_numbers[j]:
            sequence.append(list_of_numbers[i])
            j = i
    return sequence

def find_max_sequence(list_of_numbers):
    max_sequence = []
    for i in range(0, len(list_of_numbers)):
        for k in range(1, len(list_of_numbers)):
            length = len(find_sequence(list_of_numbers, i, k))
            if length > len(max_sequence):
                max_sequence = find_sequence(list_of_numbers, i, k)
    return max_sequence

numbers = [1, 5, 2, 3, 4, 6, 1, 7]
print(find_max_sequence(numbers))

numbers2 = [5, 2, 3, 4, 6, 1, 7]
print(find_max_sequence(numbers2))

