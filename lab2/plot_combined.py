from matplotlib import pyplot as plt
from sorting_time import get_times

times = get_times()

keys, values = times["mergesort"].keys(), times["mergesort"].values()
plt.plot(keys, values, "o-", label="merge sorting", ms=2)

keys, values = times["quicksort"].keys(), times["quicksort"].values()
plt.plot(keys, values, "o-", label="quick sorting", ms=2)

keys, values = times["bubblesort"].keys(), times["bubblesort"].values()
plt.plot(keys, values, "o-", label="bubble sorting", ms=2)

keys, values = times["selectionsort"].keys(), times["selectionsort"].values()
plt.plot(keys, values, "o-", label="selection sorting", ms=2)

plt.title(label="sorting")
plt.xlabel("Number of words")
plt.ylabel("Time (s)")
plt.xticks(rotation=30, fontsize="xx-small", horizontalalignment="right")
plt.legend()
plt.savefig("lab2/times_combined.png")
