def insertionSort(arr):
      
    for i in range(1, len(arr)):
  
        pos = arr[i]
       
        j = i-1
        while j >=0 and pos < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = pos
  
arr = [12, 11, 14, 10, 6, 7, 13]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])