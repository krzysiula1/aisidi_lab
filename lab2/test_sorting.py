from sorting import selectionSort, quickSort


def test_selectionSort_empty():
    data = []
    expected = []
    assert selectionSort(data) == expected


def test_selectionSort_one_word():
    data = [1]
    expected = [1]
    assert selectionSort(data) == expected


def test_selectionSort():
    data = [9, 1, 2, 4, 5, 7, 8, 6, 3, 0, 10, 11, 13, -2, 1324, -24, 123, 13, 134]
    expected = [-24, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 13, 123, 134, 1324]
    assert selectionSort(data) == expected


def test_selectionSort_text_1():
    with open("lab2/pan-tadeusz.txt", "r", encoding="utf-8") as file:
        text = file.read()
    data = text.split()[:1000]
    result = selectionSort(data)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]


def test_selectionSort_text_5():
    with open("lab2/pan-tadeusz.txt", "r", encoding="utf-8") as file:
        text = file.read()
    data = text.split()[:5000]
    result = selectionSort(data)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]


def test_quickSort_empty():
    data = []
    expected = []
    assert quickSort(data) == expected


def test_quickSort_one_word():
    data = [1]
    expected = [1]
    assert quickSort(data) == expected


def test_quickSort():
    data = [9, 1, 2, 4, 5, 7, 8, 6, 3, 0, 10, 11, 13, -2, 1324, -24, 123, 13, 134]
    expected = [-24, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 13, 123, 134, 1324]
    assert quickSort(data) == expected


def test_quickSort_text_1():
    with open("lab2/pan-tadeusz.txt", "r", encoding="utf-8") as file:
        text = file.read()
    data = text.split()[:1000]
    result = quickSort(data)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]


def test_quickSort_text_5():
    with open("lab2/pan-tadeusz.txt", "r", encoding="utf-8") as file:
        text = file.read()
    data = text.split()[:5000]
    result = quickSort(data)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]
