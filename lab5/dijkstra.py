# Python3 implementation to find the
# shortest path in a directed
# graph from source vertex to
# the destination vertex
from string import digits
from sys import argv


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


infi = 1000000000


class Node:

    def __init__(self, vertexNumber):
        self.vertexNumber = vertexNumber
        self.children = []

    def add_child(self, vNumber, length):
        self.children.append(Pair(vNumber, length))


def dijkstraDist(g, s):
    path = [0]*len(g)
    dist = [infi for i in range(len(g))]

    visited = [False for i in range(len(g))]

    for i in range(len(g)):
        path[i] = -1
    dist[s] = 0
    path[s] = -1
    current = s

    sett = set()
    while True:

        visited[current] = True
        for i in range(len(g[current].children)):
            v = g[current].children[i].first
            if visited[v]:
                continue

            sett.add(v)
            alt = dist[current] + g[current].children[i].second

            if alt < dist[v]:
                dist[v] = alt
                path[v] = current
        if current in sett:
            sett.remove(current)
        if len(sett) == 0:
            break

        minDist = infi
        index = 0

        for a in sett:
            if dist[a] < minDist:
                minDist = dist[a]
                index = a
        current = index
    return dist, path


def printPath(path, i, s, lst: list):
    if i != s:
        if path[i] == -1:
            return
        printPath(path, path[i], s, lst)
        lst.append(path[i])
    lst.append(i)
    return lst


def read_board(file):
    with open(file, "r") as txt:
        digits = []
        line = []
        for char in txt.read():
            if char != "\n":
                line.append(int(char))
            else:
                digits.append(line)
                line = []

    digits.append(line)
    return digits


def get_path(file):
    digits = read_board(file)
    v = []
    height = len(digits)
    width = len(digits[0])
    n = height * width
    l = 0
    zeros = []
    for i in digits:
        for j in i:
            if j == 0:
                zeros.append(l)
            l+=1
    [s,e] = zeros

    for i in range(n):
        v.append(Node(i))

    temp = 0
    ver = []
    ver_v = []
    for i in range(height):
        for j in range(width):
            ver_v.append(temp)
            temp += 1
        ver.append(ver_v)
        ver_v = []

    temp = 0
    for i in range(height):
        if i < height - 1:
            for j in range(width):
                if i > 0:
                    v[temp].add_child(ver[i - 1][j], digits[i - 1][j])
                if j > 0:
                    v[temp].add_child(ver[i][j - 1], digits[i][j - 1])
                if j < len(digits[0]) - 1:
                    v[temp].add_child(ver[i][j + 1], digits[i][j + 1])
                    v[temp].add_child(ver[i + 1][j], digits[i + 1][j])
                else:
                    v[temp].add_child(ver[i + 1][j], digits[i + 1][j])
                temp += 1
        else:
            for j in range(len(digits[0])):
                if i > 0:
                    v[temp].add_child(ver[i - 1][j], digits[i - 1][j])
                if j > 0:
                    v[temp].add_child(ver[i][j - 1], digits[i][j - 1])
                if j < len(digits[0]) - 1:
                    v[temp].add_child(ver[i][j + 1], digits[i][j + 1])
                temp += 1

    
    dist, path = dijkstraDist(v, s)

    lst = printPath(path, e, 0, [])

    temp = 0
    board = ""
    for i in range(len(digits)):
        for j in range(len(digits[0])):
            if temp in lst:
                board += "1 "
            else:
                board += "0 "
            temp += 1
        board += "\n"
    
    return board, s, e

if __name__ == "__main__":
    board, s, e = get_path(argv[1])
    print(f"\nShortest path --> from position {s} to position {e}:\n\n" + board)

