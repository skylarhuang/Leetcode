# Contain Duplicate I
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) < len(nums)

# Contain Duplicate II
# Wrong Answer
# Time Limit Exceeded
# O(n^2)
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k==0:
            return False
        elif len(set(nums)) == len(nums):
            return False
        else:
            tmp = []     
            for i in range(len(nums)):
                if nums[i] in tmp:
                    return True
                else:
                    if len(tmp) == k:
                        tmp.pop(0)
                    tmp.append(nums[i])
        return False

# Using Dictionary
# O(n)
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tmp = {}
        for i, num in enumerate(nums):
            if num in tmp:
                if i - tmp[num] <= k:
                    return True
            tmp[num] = i
        return False


# Contain Duplicate III