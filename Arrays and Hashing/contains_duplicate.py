from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    numsSet = set()
    for n in nums:
        if n in numsSet:
            return True
        numsSet.add(n)

    return False


def test_contains_duplicate():
    nums = [1, 2, 3, 1]
    assert contains_duplicate(nums)
    nums = [1, 2, 3]
    assert not contains_duplicate(nums)
