# Notes
## <a name="selectionsort"> Selection Sort </a> 
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
        #Compare blocks previous element with key recursively
        while ( block > 0 and a[block-1] > key):
            a[block] = a[block-1]
            block = block - 1
        a[block] = key
    return a
```

## <a name="mergesort"> Merge Sort </a>
Recursively divide the array into sub elements of possible equal sizes until they are sorted. Generally for an unsorted array, we would have to divide until there is only one element left. Once all the elements are divided, merge them comparing both left and right divisions.

```Python
def mergesort(a):
    if(len(a)>1):
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]
        #Recursively subdivide till there is only one element left
        mergesort(L)
        mergesort(R)
        #i = index of left, j = index of right, k = index of merged array
        i = j = k = 0
        #Find smallest entry comparing two divisions and insert the lowest into array at kth index
        while( i < len(L) and j < len(R)):
            if( L[i] < R[j]):
                a[k] = L[i]
                i = i + 1
            else:
                a[k] = R[j]
                j = j + 1
            k = k + 1
        #Loop if there are any left over elements in left array
        while ( i < len(L)):
            a[k] = L[i]
            k = k + 1
            i = i + 1
        #Loop if there are any left over elements in right array
        while ( j < len(R)):
            a[k] = R[j]
            k = k + 1
            j = j + 1
        return a
```
## <a name="quicksort"> Quick Sort </a>
It is the common sorting algorithm in many programming languages and the advantage of it over merge sort is that it doesn't require additional O(n) auxillary space as in merge sort. 
Pick a pivot element, usually last element, create an array such that elements less than pivot element are to the left and greater than are to the right. 
```Python
def Partition(A, begin, end):
    pivot = A[end]
    partitionIndex = begin
    for j in range(begin, end):
        if( A[j] <= pivot):
            A[j], A[partitionIndex] = A[partitionIndex], A[j]
            partitionIndex += 1
    A[partitionIndex], A[end] = A[end], A[partitionIndex]
    return partitionIndex

def QuickSort(A, begin, end):
    if( begin < end):
        partitionIndex = Partition(A, begin, end)
        QuickSort(A, begin, partitionIndex - 1)
        QuickSort(A, partitionIndex + 1, end)
    return A
``` 
