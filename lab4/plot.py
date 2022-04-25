from matplotlib import pyplot as plt
from times import get_times
import json

def get_insert_plot(times):
    keys, values = times["insert"]['2'].keys(), times["insert"]['2'].values()
    plt.plot(keys, values, "o-", label="2-arny", ms=2)

    keys, values = times["insert"]['3'].keys(), times["insert"]['3'].values()
    plt.plot(keys, values, "o-", label="3-arny", ms=2)

    keys, values = times["insert"]['4'].keys(), times["insert"]['4'].values()
    plt.plot(keys, values, "o-", label="4-arny", ms=2)

    plt.title(label="heaps")
    plt.xlabel("Number of elements")
    plt.ylabel("Time (s)")
    plt.xticks(rotation=30, fontsize="xx-small", horizontalalignment="right")
    plt.legend()
    plt.savefig("lab4/insert.png")


def get_remove_plot(times):
    keys, values = times["remove"]['2'].keys(), times["remove"]['2'].values()
    plt.plot(keys, values, "o-", label="2-arny", ms=2)

    keys, values = times["remove"]['3'].keys(), times["remove"]['3'].values()
    plt.plot(keys, values, "o-", label="3-arny", ms=2)

    keys, values = times["remove"]['4'].keys(), times["remove"]['4'].values()
    plt.plot(keys, values, "o-", label="4-arny", ms=2)

    plt.title(label="heaps")
    plt.xlabel("Number of elements")
    plt.ylabel("Time (s)")
    plt.xticks(rotation=30, fontsize="xx-small", horizontalalignment="right")
    plt.legend()
    plt.savefig("lab4/remove.png")


