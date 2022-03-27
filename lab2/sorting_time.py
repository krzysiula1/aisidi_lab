from sorting import selectionSort, quickSort, bubbleSort, mergeSort
import time
import gc

with open("lab2/pan-tadeusz.txt", "r", encoding="utf-8") as file:
    text = file.read()

data1 = text.split()[:1000]
data2 = text.split()[:2000]
data3 = text.split()[:3000]
data4 = text.split()[:4000]
data5 = text.split()[:5000]
data6 = text.split()[:6000]
data7 = text.split()[:7000]
data8 = text.split()[:8000]
data9 = text.split()[:9000]
data10 = text.split()[:10000]

data = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]


def get_selection_times():
    times = []
    for set in data:
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        selectionSort(set)
        stop = time.process_time()
        times.append(stop - start)
        if gc_old:
            gc.enable()
    return times


def get_quick_times():
    times = []
    for set in data:
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        quickSort(set)
        stop = time.process_time()
        times.append(stop - start)
        if gc_old:
            gc.enable()
    return times


def get_bubble_times():
    times = []
    for set in data:
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        bubbleSort(set)
        stop = time.process_time()
        times.append(stop - start)
        if gc_old:
            gc.enable()
    return times


def get_merge_times():
    times = []
    for set in data:
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        mergeSort(set)
        stop = time.process_time()
        times.append(stop - start)
        if gc_old:
            gc.enable()
    return times


print(f"Quicksort times: {get_quick_times()}")
print(f"Mergesort times: {get_merge_times()}")
print(f"Selectionsort times: {get_selection_times()}")
print(f"Bubblesort times: {get_bubble_times()}")
