# Global variable
num_calls = 0



def partition(user_ids, low, high):
    global num_calls
    num_calls += 1

    i = low - 1
    pivot = user_ids[high]

    for j in range(low, high):
        if user_ids[j] <= pivot:
            i += 1
            user_ids[i], user_ids[j] = user_ids[j], user_ids[i]

    user_ids[i + 1], user_ids[high] = user_ids[high], user_ids[i + 1]
    return i + 1


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if i < k:
        p = partition(user_ids, i, k)
        quicksort(user_ids, i, p - 1)
        quicksort(user_ids, p + 1, k)


if __name__ == "__main__":

    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)



