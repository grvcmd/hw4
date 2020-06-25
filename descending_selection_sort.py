# Define selection_sort_descend_trace() function.
def selection_sort_descend_trace(list):
    for i in range(len(list) - 1):
        max_index = i
        for j in range(i + 1, len(list)):
            if list[j] > list[max_index]:
                max_index = j
        list[i], list[max_index] = list[max_index], list[i]
        print(' '.join([str(x) for x in list]), '')
    return list


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)
