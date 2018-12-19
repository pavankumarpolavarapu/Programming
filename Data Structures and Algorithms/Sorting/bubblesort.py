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
a = [2, 5, 7, 1, 4, 3, 6, 8, 9]
print(bubblesort(a))