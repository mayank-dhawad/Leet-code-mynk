
class Solution(object):
    def thirdMax(self, nums):
        n = len(nums)

        # Sort in descending order using Selection Sort
        for i in range(n):
            max_index = i

            for j in range(i + 1, n):
                if nums[j] > nums[max_index]:
                    max_index = j

            nums[i], nums[max_index] = nums[max_index], nums[i]

        # Remove duplicates
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)

        # Return the third distinct maximum
        if len(unique) >= 3:
            return unique[2]
        else:
            return unique[0]
        