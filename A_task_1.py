"""Task 1 (Easy): Second Largest Distinct Number

Return the second largest distinct integer in numbers.
Return None if there are fewer than two distinct values.
Do not modify the input list.

Examples:
    [4, 1, 7, 7, 3] -> 4
    [-5, -2, -8] -> -5
    [9, 9] -> None

Constraints: 0 <= len(numbers) <= 10_000.
"""


def second_largest(numbers: list[int]) -> int | None:
    largest = second = None
    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number
    return second
    

if __name__ == "__main__":
    assert second_largest([4, 1, 7, 7, 3]) == 4
    assert second_largest([-5, -2, -8]) == -5
    assert second_largest([9, 9]) is None
    assert second_largest([]) is None
    assert second_largest([0, -1]) == -1
    print("All sample checks passed!")
