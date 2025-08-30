class Solution:
    def twoSum(self, nums, target):
        """
        Hash Map Approach - O(n) time, O(n) space
        Store complements in a hash map for O(1) lookup
        """
        complement_map = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num

            # Check if complement exists in our map
            if complement in complement_map:
                return [complement_map[complement], i]

            # Store current number and its index
            complement_map[num] = i

        return []  # This shouldn't happen given the problem constraints


# Alternative: Brute Force Solution (for reference)
class SolutionBruteForce:
    def twoSum(self, nums, target):
        """
        Brute Force Approach - O(n^2) time, O(1) space
        Check every possible pair of numbers
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# Test locally (optional - remove for LeetCode submission)
def test_solution():
    solution = Solution()
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]

    print("Testing optimal solution:")
    for nums, target in test_cases:
        result = solution.twoSum(nums, target)
        print("Input: nums = {}, target = {}".format(nums, target))
        print("Output: {}".format(result))
        print()

# Uncomment to test locally:
test_solution()
