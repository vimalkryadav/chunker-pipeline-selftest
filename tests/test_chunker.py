import pytest

from chunker import chunk


def test_exact_multiple():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_trailing_partial_chunk():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_shorter_than_size():
    assert chunk([1, 2], 5) == [[1, 2]]


def test_single_element_chunks():
    assert chunk("abc", 1) == [["a"], ["b"], ["c"]]


def test_empty():
    assert chunk([], 3) == []


def test_rejects_zero_size():
    with pytest.raises(ValueError):
        chunk([1, 2], 0)
