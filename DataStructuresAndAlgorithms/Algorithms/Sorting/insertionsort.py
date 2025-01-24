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


a = [2, 5, 7, 1, 4, 3, 6, 8, 9]
print(insertionsort(a))