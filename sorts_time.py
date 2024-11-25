import random
import time
import sorts


N = 1000000


original_array = [random.randint(1, 100000) for i in range(N)]


def measure_sort_time(sort_function, data):
    start = time.time()
    sort_function(data)
    finish = time.time()
    return (finish - start) * 1000


sort_results = {}


sort_results['Bubble Sort'] = measure_sort_time(sorts.bubble_sort, original_array.copy())
sort_results['Selection Sort'] = measure_sort_time(sorts.selection_sort, original_array.copy())
sort_results['Insertion Sort'] = measure_sort_time(sorts.insertion_sort, original_array.copy())
sort_results['Quick Sort'] = measure_sort_time(lambda x: sorts.quick_sort(x, 0, len(x) - 1), original_array.copy())
sort_results['Bose-Nelson Sort'] = measure_sort_time(sorts.bose_nelson, original_array.copy())


for sort_name, time_taken in sort_results.items():
    print(f"{sort_name}: {time_taken:.2f} мс")
