# divide and conquer algorithm
# choose a pivot element
# compare each element of the array to the pivot to split the array in 2: a previous array and a next array
# sort recursively those 2 arrays and return the result of the prev + pivot + next arrays

def quick_sort(arr):
    # if arr is size 0 or 1, it is sorted already
    if len(arr) <= 1:
        return (arr)
    # choose a pivot
    pivot = arr[0]
    prev_arr = []
    next_arr = []
    for i in range(1, len(arr)):
        # if element is less than pivot, it goes into the prev array
        if arr[i] < pivot:
            prev_arr += [arr[i]]
        # else it goes into the next array
        else:
            next_arr += [arr[i]]
    # sort both arrays recursively and append the next array to the prev them to get the result
    res = quick_sort(prev_arr) + [pivot] + quick_sort(next_arr)
    return res

# Instead of making new arrays which is very space consuming I should partition the array aroudn the pivot, put the smaller items before pivot and higher after pivot