from sorting import selectionSort, quickSort, bubbleSort, mergeSort
import time
import gc
import json


def get_selection_times(data):
    times = {}
    for set in data.keys():
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        selectionSort(data[set])
        stop = time.process_time()
        times[set] = stop - start
        if gc_old:
            gc.enable()
    return times


def get_quick_times(data):
    times = {}
    for set in data.keys():
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        quickSort(data[set])
        stop = time.process_time()
        times[set] = stop - start
        if gc_old:
            gc.enable()
    return times


def get_bubble_times(data):
    times = {}
    for set in data.keys():
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        bubbleSort(data[set])
        stop = time.process_time()
        times[set] = stop - start
        if gc_old:
            gc.enable()
    return times


def get_merge_times(data):
    times = {}
    for set in data.keys():
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        mergeSort(data[set])
        stop = time.process_time()
        times[set] = stop - start
        if gc_old:
            gc.enable()
    return times


def get_times():
    with open("lab2/pan-tadeusz.txt", "r", encoding="utf-8") as file:
        text = file.read()

    data = {
        1000: text.split()[:1000],
        2000: text.split()[:2000],
        3000: text.split()[:3000],
        4000: text.split()[:4000],
        5000: text.split()[:5000],
        6000: text.split()[:6000],
        7000: text.split()[:7000],
        8000: text.split()[:8000],
        9000: text.split()[:9000],
        10000: text.split()[:10000],
    }

    times = {}
    times["quicksort"] = get_quick_times(data)
    times["mergesort"] = get_merge_times(data)
    times["selectionsort"] = get_selection_times(data)
    times["bubblesort"] = get_bubble_times(data)

    with open("lab2/times.json", "w") as file:
        json.dump(times, file)

    return times
