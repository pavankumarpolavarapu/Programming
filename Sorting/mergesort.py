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

a = [2, 5, 7, 1, 4, 3, 6, 8, 9]
print(mergesort(a))
