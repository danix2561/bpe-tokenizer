def get_stats(ids: list[int]) -> dict[tuple[int, int], int]:
    """Count how often each adjacent pair appears in ids."""
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts


def merge(ids: list[int], pair: tuple[int, int], new_id: int) -> list[int]:
    """Replace every occurrence of pair in ids with new_id."""
    out = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and (ids[i], ids[i + 1]) == pair:
           out.append(new_id)
           i=i+2
        else:
            out.append(ids[i])
            i=i+1
    return out

def train(text: str, vocab_size: int) -> dict[tuple[int, int], int]:
    """Learn BPE merges. Return {pair: new_id}, in the order created."""
    ids = list(text.encode("utf-8"))
    merges = {}
    for step in range(vocab_size - 256):
        stats = get_stats(ids)
        if not stats:
            break
        pair = max(stats, key=stats.get)
        new_id = 256 + step
        ids = merge(ids, pair, new_id)
        merges[pair]=new_id
    return merges