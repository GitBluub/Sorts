def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    left_index = 0
    right_index = 0
    index = 0
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            arr[index] = left_arr[left_index]
            left_index += 1
        else:
            arr[index] = right_arr[right_index]
            right_index += 1
        index += 1
    while left_index < len(left_arr):
        arr[index] = left_arr[left_index]
        index += 1
        left_index += 1
    
    while right_index < len(right_arr):
        arr[index] = right_arr[right_index]
        index += 1
        right_index += 1