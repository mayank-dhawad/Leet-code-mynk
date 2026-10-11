
class Solution(object):
    def targetIndices(self, nums, target):
        n = len(nums)

        # Sort in ascending order using Selection Sort
        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j

            nums[i], nums[min_index] = nums[min_index], nums[i]

        # Find all indices of target
        result = []

        for i in range(n):
            if nums[i] == target:
                result.append(i)

        return result