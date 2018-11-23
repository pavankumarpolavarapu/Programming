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
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]           
    return a 
```