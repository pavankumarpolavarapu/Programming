def selectionsort(a, n):
    for i in range(len(a)):
        iMin = i
        for j in range(i+1, len(a)):
            if a[iMin] > a[j]:
                iMin = j
        a[i], a[iMin] = a[iMin], a[i]
    return a

a = [2, 5, 7, 1, 4, 3, 6]
print(selectionsort(a, len(a)))