def bubble_sort(a):
    n = len(a)
    unordered = True
    while unordered:
        unordered = False
        for j in range(n - 1):
            if a[j] > a[j + 1]:  #сравниваются соседние элементы
                a[j], a[j + 1] = a[j + 1], a[j] #соседние элементы меняются местами
                unordered = True
        n -= 1
    return a


def selection_sort(a):
    for i in range(len(a) - 1):
        imin = i
        for j in range(i + 1, len(a)): #ищем минимальный элемент
            if a[j] < a[imin]:
                imin = j
        a[i], a[imin] = a[imin], a[i]  #когда нашли - меняем местами чтоб минимальный был вначале
    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i] #берём последний отсортированный элемент
        j = i - 1  #счётчик
        while j >= 0 and a[j] > tmp: #проверяем что счётчик не закончился и элемент счётчика не отсортирован, те больше отсортированной части
            a[j + 1] = a[j]  #меняем местами неотсортированные части
            j -= 1
        a[j + 1] = tmp  #берём новый последний отсортированный элемент
    return a


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1) #сортируется левая часть
        quick_sort(arr, pivot_index + 1, high) #сортируется правая часть


def partition(arr, low, high):
    pivot = arr[low]  # Опорный элемент — первый элемент
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:  #если элемент меньше опорного
            arr[i], arr[j] = arr[j], arr[i]  #элементы меняются местами
            i += 1  #счётчик
    arr[low], arr[i - 1] = arr[i - 1], arr[low] #меняем опорный элемент на последний
    return i - 1  # Возвращаем индекс опорного элемента


def bose_nelson(data):
    m = 1 #размер груп, которые будут сортироваться
    while m < len(data):
        j = 0
        while j + m < len(data):
            bose_nelson_merge(data, j, m, m)
            j = j + m + m
        m = m + m
    return data


def bose_nelson_merge(data, j, r, m):
    if j + r < len(data): #если индексы находятся в пределах массива
        if m == 1:
            if data[j] > data[j + r]: #сравниваем 2 элемента
                data[j], data[j + r] = data[j + r], data[j]  #меняем их местами
        else:
            m = m // 2 #уменьшаем размер группы вдвое
            bose_nelson_merge(data, j, r, m)   #слияние мелких групп
            if j + r + m < len(data):
                bose_nelson_merge(data, j + m, r, m)
            bose_nelson_merge(data, j + m, r - m, m)
    return data