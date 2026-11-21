"""Task 2 (Easy): Normalized Palindrome

Return True if text reads the same forward and backward after removing
non-alphanumeric characters and ignoring case. Use only ASCII input.
An empty string after normalization counts as a palindrome.

Examples:
    "A man, a plan, a canal: Panama!" -> True
    "race a car" -> False
    "!!!" -> True

Constraints: 0 <= len(text) <= 10_000.
"""


def is_palindrome(text: str) -> bool:
    normalized = "".join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama!") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome("!!!") is True
    assert is_palindrome("") is True
    assert is_palindrome("1a2") is False
    assert is_palindrome("0P") is False
    print("All sample checks passed!")
