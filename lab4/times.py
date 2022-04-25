import random
from heap import Heap
import time
import gc
import json


def check_insert_time(data, arny):
    times = {}
    for set in data:
        gc_old = gc.isenabled()
        gc.disable()
        heap = Heap(arny)
        start = time.process_time()
        for value in data[set]:
            heap.insert(value)
        stop = time.process_time()
        times[set] = stop - start
        if gc_old:
            gc.enable()
        print(set)
    print(arny)
    return times

def check_remove_time(data, arny):
    times = {}
    for set in data:
        gc_old = gc.isenabled()
        gc.disable()
        heap = Heap(arny)
        for value in data[set]:
            heap.insert(value)
        start = time.process_time()
        for i in range(set):
            heap.remove_top()
        stop = time.process_time()
        times[set] = stop - start
        if gc_old:
            gc.enable()
        print(set)
    print(arny)
    return times




def get_times():
    values = random.sample(range(300_000), 100_000)

    data = {
        10_000: values[:10_000],
        20_000: values[:20_000],
        30_000: values[:30_000],
        40_000: values[:40_000],
        50_000: values[:50_000],
        60_000: values[:60_000],
        70_000: values[:70_000],
        80_000: values[:80_000],
        90_000: values[:90_000],
        100_000: values[:100_000],
    }

    times = {}
    times['insert'] = {}
    times['remove'] = {}
    times["insert"]['2'] = check_insert_time(data, 2)
    times["insert"]['3'] = check_insert_time(data, 3)
    times["insert"]['4'] = check_insert_time(data, 4)
    times["remove"]['2'] = check_remove_time(data, 2)
    times["remove"]['3'] = check_remove_time(data, 3)
    times["remove"]['4'] = check_remove_time(data, 4)

    with open("lab4/times.json", "w") as file:
        json.dump(times, file)

    return times

#get_times()

