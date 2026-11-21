"""Task 6 (Medium): Longest Substring Without Repeats

Return the length of the longest contiguous substring containing no
repeated characters. Characters are case-sensitive; spaces count.

Examples:
    "abcabcbb" -> 3
    "bbbbb" -> 1
    "pwwkew" -> 3

Constraints: 0 <= len(text) <= 100_000; ASCII input.
Target: O(n) time.
"""


def longest_unique_substring(text: str) -> int:...

if __name__ == "__main__":
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("abba") == 2
    assert longest_unique_substring("aA b") == 4
    print("All sample checks passed!")
