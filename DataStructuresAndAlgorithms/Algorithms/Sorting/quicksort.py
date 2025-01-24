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
a = [2, 5, 7, 1, 4, 3, 6, 8, 9]
print(QuickSort(a, 0, len(a) - 1))
