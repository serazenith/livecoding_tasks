"""Task 3 (Easy): Run-Length Encoding

Encode each consecutive run of identical characters as the character
followed by its count, including runs of length one.
The input contains only lowercase English letters.

Examples:
    "aaabbcaa" -> "a3b2c1a2"
    "abc" -> "a1b1c1"
    "" -> ""

Constraints: 0 <= len(text) <= 100_000.
"""


def encode_runs(text: str) -> str:
    if not text:
        return ""
    
    encoded = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    encoded.append(f"{current_char}{count}")
    
    return "".join(encoded)
    


if __name__ == "__main__":
    assert encode_runs("aaabbcaa") == "a3b2c1a2"
    assert encode_runs("abc") == "a1b1c1"
    assert encode_runs("") == ""
    assert encode_runs("z") == "z1"
    assert encode_runs("a" * 12) == "a12"
    print("All sample checks passed!")
