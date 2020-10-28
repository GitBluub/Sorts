from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort

arr = [64, 34, 25, 12, 22, 11, 90, -12] 
  
# bubble_sort(arr) 
# arr = quick_sort(arr)
# merge_sort(arr)
insertion_sort(arr)
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]), 