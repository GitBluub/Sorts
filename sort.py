from bubble_sort import bubble_sort
from quick_sort import quick_sort

arr = [64, 34, 25, 12, 22, 11, 90, -12] 
  
# bubble_sort(arr) 
arr = quick_sort(arr)
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]), 