from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    prev_map = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [i, prev_map[diff]]
        prev_map[n] = i

    return []


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
