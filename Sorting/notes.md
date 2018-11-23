# Notes
## <a href="selectionsort"> Selection Sort </a> 
Iteratively find the least element and put it in a new array and replace the existing element with largest value. (not In place)
For In Place, iteratively find the least element and swap the position with one position after last sorted element.
```Python
def selectionsort(a, n):
    for i in range(len(a)):
        iMin = i
        for j in range(i+1, len(a)):
            if a[iMin] > a[j]:
                iMin = j
        a[i], a[iMin] = a[iMin], a[i]
    return a
```
## <a name="bubblesort">Bubble Sort</a>
Bubble sort recursively compares the next element and swaps if following element is smaller. The largest number bubbles at the end and after every pass last i elements are largest among the array. We will only loop till n-i-1 because, there won't be any n-i entry for comparison.
 
```Python
def bubblesort(a):
    for i in range(len(a)):
        swapped = False
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if (swapped == False):
            break       
    return a
```

## <a name="insertionsort">Insertion Sort</a>
Recursively compare the next element and swap left till it's correct position in sequence. To do so, the best possible approach would be to copy the current element to a temporary variable and assume empty block on the current element. Recursively compare the empty block - 1 element with key, if empty block -1 is lesser than key, shift the empty block left

```Python
def insertionsort(a):
    for i in range(1, len(a)):
        key = a[i]
        block = i
        while ( block > 0 and a[block-1] > key):
            a[block] = a[block-1]
            block = block - 1
        a[block] = key
    return a