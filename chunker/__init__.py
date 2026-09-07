"""Small helpers for splitting sequences."""

__all__ = ["chunk"]


def chunk(items, size):
    """Split *items* into consecutive lists of length *size*.

    The final list is shorter when ``len(items)`` is not a multiple of *size*.

    >>> chunk([1, 2, 3, 4], 2)
    [[1, 2], [3, 4]]
    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    if size < 1:
        raise ValueError("size must be >= 1")
    out = []
    for start in range(0, len(items), size):
        out.append(list(items[start:start + size]))
    return out
