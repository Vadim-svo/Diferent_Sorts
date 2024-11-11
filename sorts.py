def bubble_sort(a):
    """Сортировка списка с помощью алгоритма пузырьковой сортировки."""
    n = len(a)
    unordered = True
    while unordered:
        unordered = False
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # Обмен значениями
                unordered = True
                print(a)  # Печать списка после изменения
        n -= 1  # Уменьшаем диапазон сравнения
    return a  # Возврат отсортированного массива


def selection_sort(a):
    """Сортировка списка с помощью алгоритма сортировки выбором."""
    for i in range(len(a) - 1):
        imin = i  # Предполагаем, что минимальный — первый элемент
        for j in range(i + 1, len(a)):
            if a[j] < a[imin]:
                imin = j  # Обновляем индекс минимального элемента
        a[i], a[imin] = a[imin], a[i]  # Обмен значениями
        print(a)  # Печать списка после изменения
    return a


def insertion_sort(a):
    """Сортировка списка с помощью алгоритма сортировки вставками."""
    for i in range(1, len(a)):
        tmp = a[i]
        j = i - 1
        while j >= 0 and a[j] > tmp:  # Перемещаем элементы, которые больше tmp
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = tmp  # Устанавливаем tmp на своё место
        print(a)  # Печать списка после изменения
    return a


def quick_sort(arr, low=0, high=None):
    """Сортировка списка с помощью алгоритма быстрой сортировки."""
    if high is None:
        high = len(arr) - 1  # Установка high на последний индекс

    if low < high:
        pivot_index = partition(arr, low, high)
        print(arr)  # Печать списка после изменения в каждом разделении
        quick_sort(arr, low, pivot_index - 1)  # Рекурсивная сортировка левой части
        quick_sort(arr, pivot_index + 1, high)  # Рекурсивная сортировка правой части
    return arr  # Возврат отсортированного массива


def partition(arr, low, high):
    """Помощник для разделения массива в быстрой сортировке."""
    pivot = arr[low]  # Опорный элемент — первый элемент
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Обмен
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Перемещение опорного элемента на его правильную позицию
    return i - 1  # Возврат индекса опорного элемента


def bose_nelson(data):
    """Сортировка списка с помощью алгоритма Бозе-Нельсона."""
    m = 1
    while m < len(data):
        j = 0
        while j + m < len(data):
            bose_nelson_merge(data, j, m, m)  # Слияние подмассивов
            print(data)  # Печать списка после изменения
            j += m + m
        m += m
    return data


def bose_nelson_merge(data, j, r, m):
    """Помощник для слияния подмассивов в алгоритме Бозе-Нельсона."""
    if j + r < len(data):
        if m == 1:
            if data[j] > data[j + r]:
                data[j], data[j + r] = data[j + r], data[j]  # Обмен, если нужно
        else:
            m //= 2  # Делим m на два для следующего уровня рекурсии
            bose_nelson_merge(data, j, r, m)
            if j + r + m < len(data):
                bose_nelson_merge(data, j + m, r, m)
            bose_nelson_merge(data, j + m, r - m, m)
    return data
