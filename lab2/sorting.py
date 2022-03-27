def selectionSort(data):
    length = len(data)
    for i in range(length):
        min_value_id = i
        for j in range(i + 1, length):
            if data[j] < data[min_value_id]:
                min_value_id = j
        (data[i], data[min_value_id]) = (data[min_value_id], data[i])
    return data


def quickSort(data):
    def partition(data, low, high):
        pivot_id = high
        pivot_value = data[pivot_id]
        boarder = low
        for i in range(low, high):
            if data[i] <= pivot_value:
                (data[i], data[boarder]) = (data[boarder], data[i])
                boarder += 1

        (data[high], data[boarder]) = (data[boarder], data[high])
        return boarder

    def sort(data, low, high):
        if high > low:
            boarder = partition(data, low, high)
            sort(data, low, boarder - 1)
            sort(data, boarder + 1, high)
        return data

    return sort(data, 0, len(data) - 1)


def bubbleSort(board):
    for i in range(len(board) - 1):
        for j in range(0, len(board) - i - 1):
            if board[j] > board[j + 1]:
                board[j], board[j + 1] = board[j + 1], board[j]

    return board


def mergeSort(board):
    if len(board) > 1:
        mid = len(board) // 2
        left = board[:mid]
        right = board[mid:]

        mergeSort(right)
        mergeSort(left)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                board[k] = left[i]
                i += 1
            else:
                board[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            board[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            board[k] = right[j]
            j += 1
            k += 1

        return board
