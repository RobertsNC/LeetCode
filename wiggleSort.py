import numpy as np


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    return nums


def wiggleSort(nums):
    nums = sorted(nums)
    print(nums)
    for i in range(1, len(nums) - 1, 2):
        nums = swap(nums, i, i + 1)
    return nums


def smartSol(nums):
    less = True
    for i in range(0, len(nums) - 1):
        if less:
            if nums[i] > nums[i + 1]:
                swap(nums, i, i + 1)
        else:
            if nums[i] < nums[i + 1]:
                swap(nums, i, i + 1)
        less = not(less)
    return nums


def bruteForce():
    nums = [3, 5, 2, 1, 6, 4]
    wiggle = wiggleSort(nums)
    print(wiggle)


def singlePass():
    nums = [3, 5, 2, 1, 6, 4]
    wiggle = smartSol(nums)
    print(wiggle)


if __name__ == '__main__':
    singlePass()
