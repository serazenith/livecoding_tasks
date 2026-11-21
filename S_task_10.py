"""Task 10 (Hard): Minimum Covering Window

Return the shortest contiguous substring of text containing every character
of required, including its multiplicity. Extra characters are allowed.
Characters are case-sensitive. If multiple shortest windows exist, return
the earliest one in text. Return "" if no window exists or required is empty.

Examples:
    text="ADOBECODEBANC", required="ABC" -> "BANC"
    text="AAABBC", required="AABC" -> "AABBC"
    text="a", required="aa" -> ""

Constraints: 0 <= len(text), len(required) <= 100_000; ASCII input.
Target: O(len(text) + len(required)) time.
"""


def minimum_window(text: str, required: str) -> str:
    if not required:
        return ""
    
    from collections import Counter
    
    required_count = Counter(required)
    required_length = len(required_count)
    
    left = 0
    right = 0
    formed = 0
    window_counts = {}
    
    min_length = float("inf")
    min_window = (0, 0)
    
    while right < len(text):
        char = text[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in required_count and window_counts[char] == required_count[char]:
            formed += 1
        
        while left <= right and formed == required_length:
            char = text[left]
            
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = (left, right)
            
            window_counts[char] -= 1
            if char in required_count and window_counts[char] < required_count[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if min_length == float("inf") else text[min_window[0]:min_window[1] + 1]


if __name__ == "__main__":
    assert minimum_window("ADOBECODEBANC", "ABC") == "BANC"
    assert minimum_window("AAABBC", "AABC") == "AABBC"
    assert minimum_window("a", "aa") == ""
    assert minimum_window("a", "a") == "a"
    assert minimum_window("abxxba", "ab") == "ab"
    assert minimum_window("aA", "A") == "A"
    assert minimum_window("abc", "") == ""
    assert minimum_window("", "a") == ""
    print("All sample checks passed!")
