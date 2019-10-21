# Сортировка слиянием
def merge_sort(array):
    if len(array) < 2:
        return array

    # Разбиваем входной массив на первую и вторую части и сортируем каждую из них.
    first_part = merge_sort(array[0: len(array) // 2])
    second_part = merge_sort(array[len(array) // 2: len(array)])

    # Смешиваем обе части в один отсортированный массив
    i = j = 0
    sorted_array = []
    while i < len(first_part) or j < len(second_part):
        if not i < len(first_part):
            sorted_array.append(second_part[j])
            j += 1
        elif not j < len(second_part):
            sorted_array.append(first_part[i])
            i += 1
        elif first_part[i] < second_part[j]:
            sorted_array.append(first_part[i])
            i += 1
        else:
            sorted_array.append(second_part[j])
            j += 1

    return sorted_array


# Конец сортировки слиянием


print(my_list)
start_time = datetime.now()
print("\n Сортировка слиянием\n")
print(merge_sort(my_list))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


# Сортировка кучей
def create_heap(array, heap_size, root_index):
    max_index = root_index
    left_child_index = (2 * root_index) + 1
    right_child_index = (2 * root_index) + 2

    if (left_child_index < heap_size) and (array[left_child_index] > array[max_index]):
        max_index = left_child_index
    if (right_child_index < heap_size) and (array[right_child_index] > array[max_index]):
        max_index = right_child_index
    if max_index != root_index:
        array[root_index], array[max_index] = array[max_index], array[root_index]
        create_heap(array, heap_size, max_index)


def heap_sort(array):
    sorted_array = array
    for i in range(len(sorted_array), -1, -1):
        create_heap(sorted_array, len(sorted_array), i)
    for i in range(len(sorted_array) - 1, 0, -1):
        sorted_array[i], sorted_array[0] = sorted_array[0], sorted_array[i]
        create_heap(sorted_array, i, 0)
    return sorted_array


# Конец сортировки кучей


start_time = datetime.now()
print("\n Сортировка кучей\n")
print(heap_sort(my_list))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))


### Быстрая сортировка
def quick_sort(array):
    sorted_array = array

    def _quick_sort(array_, smaller_value_index, bigger_value_index):
        if smaller_value_index < bigger_value_index:
            # Это индекс после опорного элемента, по которому наши списки разделены
            split_index = partition(array_, smaller_value_index, bigger_value_index)
            _quick_sort(array_, smaller_value_index, split_index)
            _quick_sort(array_, split_index + 1, bigger_value_index)

    _quick_sort(sorted_array, 0, len(sorted_array) - 1)
    return sorted_array


def partition(array, smaller_value_index, bigger_value_index):
    central = array[(smaller_value_index + bigger_value_index) // 2]
    i = smaller_value_index - 1
    j = bigger_value_index + 1
    while True:
        i += 1
        while array[i] < central:
            i += 1
        j -= 1
        while array[j] > central:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


### Конец быстрой сортировки


start_time = datetime.now()
print("\n Быстрая сортировка\n")
print(quick_sort(my_list))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))