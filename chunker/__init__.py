"""Small helpers for splitting sequences."""

__all__ = ["chunk"]


def chunk(items, size):
    """Split *items* into consecutive lists of length *size*.

    >>> chunk([1, 2, 3, 4], 2)
    [[1, 2], [3, 4]]
    """
    if size < 1:
        raise ValueError("size must be >= 1")
    out = []
    for start in range(0, len(items) - size + 1, size):
        out.append(list(items[start:start + size]))
    return out
