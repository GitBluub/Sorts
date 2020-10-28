def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr