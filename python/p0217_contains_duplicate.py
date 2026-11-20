"""Hash set of seen values; exit as soon as a duplicate appears. O(n) time, O(n) space."""
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False


def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1])
    assert not contains_duplicate([1, 2, 3, 4])
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    assert not contains_duplicate([7])
    assert contains_duplicate([-1, -1])
