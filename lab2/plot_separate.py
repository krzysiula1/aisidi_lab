from matplotlib import pyplot as plt
from sorting_time import get_times

times = get_times()
fig, axs = plt.subplots(2, 2)

keys, values = times["mergesort"].keys(), times["mergesort"].values()
axs[0, 0].plot(keys, values)
axs[0, 0].set_title("mergesort")

keys, values = times["quicksort"].keys(), times["quicksort"].values()
axs[0, 1].plot(keys, values, "tab:orange")
axs[0, 1].set_title("quicksort")

keys, values = times["bubblesort"].keys(), times["bubblesort"].values()
axs[1, 0].plot(keys, values, "tab:green")
axs[1, 0].set_title("bubblesort")

keys, values = times["selectionsort"].keys(), times["selectionsort"].values()
axs[1, 1].plot(keys, values, "tab:red")
axs[1, 1].set_title("selectionsort")

for ax in axs.flat:
    ax.set(xlabel="Number of words", ylabel="Times (s)")

fig.tight_layout()

plt.savefig("lab2/times_separate.png")
