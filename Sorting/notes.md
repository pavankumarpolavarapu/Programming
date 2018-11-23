# Notes
## <a href="selectionsort"> Selection Sort </a> 
Iteratively find the least element and put it in a new array and replace the existing element with largest value. (not In place)
For In Place, iteratively find the least element and swap the position with one position after last sorted element.

for i in range(len(a)):
    iMin = i
    for j in range(i+1, len(a)):
        if a[iMin] > a[j]:
            iMin = j
    a[i], a[iMin] = a[iMin], a[i]

## <a name="bubblesort">Bubble Sort</a>
Bubble sort recursively compares the next element and swaps if following element is smaller.

for i in range(a):
    swapped = True
    for j in range(0, n-i-1)
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]