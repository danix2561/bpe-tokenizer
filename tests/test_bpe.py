from bpe import get_stats, merge

def test_get_stats():
    assert get_stats([1, 2, 3, 1, 2])[(1, 2)] == 2

def test_merge_basic():
    assert merge([1, 2, 3, 1, 2], (1, 2), 99) == [99, 3, 99]

def test_merge_overlap():
    assert merge([1, 1, 1], (1, 1), 99) == [99, 1]