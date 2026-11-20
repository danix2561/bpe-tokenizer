from bpe import get_stats, merge, train


def test_get_stats():
    assert get_stats([1, 2, 3, 1, 2]) == {(1, 2): 2, (2, 3): 1, (3, 1): 1}


def test_merge_basic():
    assert merge([1, 2, 3, 1, 2], (1, 2), 99) == [99, 3, 99]


def test_merge_overlap():
    assert merge([1, 1, 1], (1, 1), 99) == [99, 1]


def test_train_example():
    assert train("aaabdaaabac", 259) == {
        (97, 97): 256,
        (256, 97): 257,
        (257, 98): 258,
    }