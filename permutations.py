'''
Given an array nums of distinct integers, return all the possible permutations.You can return the answer in any order.
Example 1:
Input: nums = [1, 2, 3, 4]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''

nums = [1, 3, 5]
result = []


def permutation(nums1):
    backtrack(nums, [])
    return result


def backtrack(nums1, list1):
    if not nums1:
        result.append(list1)
    for x in range(len(nums1)):
        backtrack(nums1[:x] + nums1[x + 1:], list1 + [nums1[x]])


print(permutation(nums))
