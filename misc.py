from typing import *


def is_happy(n: int) -> bool:
    loop = set()
    while n != 1:
        loop.add(n)
        digits = [int(digit) for digit in str(n)]
        n = sum([digit**2 for digit in digits])
        if n in loop:
            return False
    return True


def twoSum(nums: List[int], target: int) -> List[int]:
    max_ = len(nums)
    for x_index in range(max_):
        for y_index in range(x_index+1, max_):
            if nums[x_index] + nums[y_index] == target:
                return [x_index, y_index]


def isometric_string(s, t):
    if len(s) != len(t):
        return False
    mapped = {}
    index = 0
    for char in s:
        if (char in mapped.keys()) or (t[index] in mapped.values()):
            try:
                if t[index] != mapped[char]:
                    return False
            except KeyError:
                return False
        else:
            mapped[char] = t[index]
        index += 1
    return True