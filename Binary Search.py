""" Binary Search
    Created on 30 april 2020
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


def binary_search(start_point, steps, search_key, found_array, sorted_data):
    if search_key != search_item:
        if search_key not in found_array:
            if search_key > search_item:
                found_array.append(search_key)
                steps = round(steps / 2)
                start_point = int(start_point - steps)
                search_key = sorted_data[start_point]
                return binary_search(start_point, steps, search_key, found_array, sorted_data)
            elif search_key < search_item:
                found_array.append(search_key)
                steps = round(steps / 2)
                start_point = int(start_point + steps)
                search_key = sorted_data[start_point]
                return binary_search(start_point, steps, search_key, found_array, sorted_data)
        else:
            result = False
            return result
    else:
        result = start_point
        return result


def search(sorted_data):
    length = len(sorted_data)
    start = int(round(length / 2))
    step = start
    key = sorted_data[start]
    found_array = []
    index = binary_search(start, step, key, found_array, sorted_data)
    return index


data = map(int, raw_input("Enter the data, separated by commas: ").split(','))
search_item = int(raw_input("Enter the number you want to search for: "))

sorted_data = quick_sort(data)

answer = search(sorted_data)

if not answer:
    print("\nThe item you are searching for does not exist in the array.")
else:
    print("\nThe item you are looking for exists! The index of your search-item is: %d in the sorted(!) data list" % answer)
