def bubblesort(a):
    for i in range(len(a)):
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]           
    return a
a = [2, 5, 7, 1, 4, 3, 6]
print(bubblesort(a))