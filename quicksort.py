""" Quicksort
    Created on 27 april 2020
    @author: Gideon Rouwendaal
    @python_version: Python 2.7
    """

def sort(pivot_index, pivot, to_be_sorted_array):
    result = [pivot]
    for i in range(len(to_be_sorted_array)):
        if i != pivot_index:
            if pivot > to_be_sorted_array[i]:
                result.insert(0, to_be_sorted_array[i])
            else:
                result.append(to_be_sorted_array[i])
    return result


def sort_bigger_then_pivot(pivot, temporary_sorted_array):
    if len(temporary_sorted_array[temporary_sorted_array.index(pivot):]) > 1:
        bigger_then_data = temporary_sorted_array[temporary_sorted_array.index(pivot) + 1:]
        return quick_sort(bigger_then_data)


def sort_smaller_then_pivot(pivot, temporary_sorted_array):
    if len(temporary_sorted_array[:temporary_sorted_array.index(pivot)]) > 0:
        smaller_then_data = temporary_sorted_array[:temporary_sorted_array.index(pivot)]
        return quick_sort(smaller_then_data)


def quick_sort(to_be_sorted_array):
    pivot_index = int(round(len(to_be_sorted_array) / 2))
    pivot_data = to_be_sorted_array[pivot_index]
    final = [pivot_data]
    if len(to_be_sorted_array) == 1:
        return to_be_sorted_array
    temporary_sorted_array = sort(pivot_index, pivot_data, to_be_sorted_array)
    if len(to_be_sorted_array) == 2:
        return temporary_sorted_array
    else:
        bigger_then = sort_bigger_then_pivot(pivot_data, temporary_sorted_array)
        smaller_then = sort_smaller_then_pivot(pivot_data, temporary_sorted_array)

    for i in range(len(bigger_then)):
        final.append(bigger_then[i])
    for i in range(len(smaller_then)):
        final.insert(0, smaller_then[-1 - i])
    return final

data = 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 16, 17, 21, 22, 23, 25, 27, 28, 30, 34, 35, 37, 38, 40, 42, 44, 45, 47, 48, 52, 53, 54, 55, 56, 58, 59, 60, 62, 73, 79, 81, 83, 84, 85, 89, 91, 94, 96, 97, 100

test = quick_sort(data)

print test