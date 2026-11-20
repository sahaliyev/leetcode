"""Subtract a value if a larger one follows, otherwise add. O(n) time, O(1) space."""
VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(s: str) -> int:
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and VALUES[s[i + 1]] > VALUES[s[i]]:
            result -= VALUES[s[i]]
        else:
            result += VALUES[s[i]]
    return result


def test_roman_to_int():
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("MMMCMXCIX") == 3999
