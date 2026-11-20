"""Reverse half of the digits. O(log n) time, O(1) space."""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    if x % 10 == 0 and x != 0:
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x = x // 10

    return x == reversed_half or x == reversed_half // 10


def test_is_palindrome():
    assert is_palindrome(121)
    assert is_palindrome(1221)
    assert is_palindrome(0)
    assert not is_palindrome(-121)
    assert not is_palindrome(10)
    assert not is_palindrome(123)
