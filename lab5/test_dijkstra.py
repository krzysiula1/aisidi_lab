from dijkstra import get_path, read_board
import pytest


def test_read_file():
    filename = "board1.txt"
    digits = read_board(filename)
    expected = [[1,1,1,1,2,2],
                [1,0,4,1,2,2],
                [9,4,2,1,1,1],
                [9,9,6,4,1,1],
                [9,9,0,4,1,1],
                [9,9,1,1,1,1]
    ]
    assert digits == expected

def test_one_0():
    filename = "board_one_0.txt"
    with pytest.raises(ValueError):
        board, s, e = get_path(filename)

def test_no_0():
    filename = "board_no_0.txt"
    with pytest.raises(ValueError):
        board, s, e = get_path(filename)

def test_over_2_0():
    filename = "board_over_2_0.txt"
    with pytest.raises(ValueError):
        board, s, e = get_path(filename)


def test_start_and_end():
    filename = "board2.txt"
    board, s, e = get_path(filename)
    assert (s == 5)
    assert (e == 11)
    

def test_shortest_path():
    filename = "board2.txt"
    board, s, e = get_path(filename)
    expected = "0 1 1 1 \n0 1 0 1 \n0 0 0 1 \n"
    print(expected)
    print(board)
    assert board == expected


def test_shortest_path_2():
    filename = "board3.txt"
    board, s, e = get_path(filename)
    expected = "1 0 1 1 1 \n1 1 1 0 1 \n"
    print(expected)
    print(board)
    assert board == expected