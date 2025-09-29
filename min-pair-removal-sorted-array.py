# LeetCode 3507: Minimum Pair Removal to Sort Array I

# SCENARIO: Manufacturing Defect Resolution System
# You're developing quality control software for a factory assembly line where products
# move through stations in sequence. Each station has a quality score, but sometimes
# adjacent stations have conflicting processes that create defects (represented by the
# sum of their scores). When defects occur, you must merge those two stations into one
# combined process, but this reduces production capacity. Your goal is to reorganize
# the assembly line into a smooth, non-decreasing quality progression (later stations
# should not have lower quality than earlier ones) using the minimum number of station
# merges. You must always merge the pair causing the worst defect (minimum sum) first,
# and if multiple pairs tie, merge the leftmost one. This optimization minimizes
# production disruption while ensuring quality standards across the entire line.

class Solution:
    # Approach 1: Simulation (Following the rules exactly)
    def minOperations(self, nums):
        """
        Simulate the process: repeatedly find minimum sum pair and merge.
        """
        operations = 0
        
        while not self.is_non_decreasing(nums):
            # Find the adjacent pair with minimum sum
            min_sum = float('inf')
            min_idx = -1
            
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i
            
            # Merge the pair at min_idx
            nums[min_idx] = nums[min_idx] + nums[min_idx + 1]
            nums.pop(min_idx + 1)
            
            operations += 1
        
        return operations
    
    def is_non_decreasing(self, arr):
        """Check if array is non-decreasing"""
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
    
    # Approach 2: Optimized with Early Termination
    def minOperations_optimized(self, nums):
        """
        Same simulation but with optimizations for checking.
        """
        nums = nums[:]  # Work on copy
        operations = 0
        
        while True:
            # Check if already sorted
            is_sorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                break
            
            # Find minimum sum pair
            min_sum = float('inf')
            min_idx = -1
            
            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i
            
            # Merge
            nums[min_idx] += nums[min_idx + 1]
            del nums[min_idx + 1]
            operations += 1
        
        return operations
    
    # Approach 3: With Detailed Tracking (Educational)
    def minOperations_verbose(self, nums):
        """
        Track each step for understanding the algorithm.
        """
        nums = nums[:]  # Work on copy
        operations = 0
        steps = []
        
        while not self.is_non_decreasing(nums):
            # Find minimum sum pair
            pairs = []
            for i in range(len(nums) - 1):
                pairs.append((i, nums[i] + nums[i + 1]))
            
            # Find minimum (leftmost if tie)
            min_idx = min(pairs, key=lambda x: x[1])[0]
            min_sum = pairs[min_idx][1]
            
            # Record step
            steps.append({
                'before': nums[:],
                'merge_idx': min_idx,
                'pair': (nums[min_idx], nums[min_idx + 1]),
                'sum': min_sum
            })
            
            # Merge
            nums[min_idx] = min_sum
            nums.pop(min_idx + 1)
            operations += 1
        
        return operations

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([5, 2, 3, 1], 2),          # Example 1
        ([1, 2, 2], 0),             # Example 2: already sorted
        ([3, 2, 1], 2),             # Decreasing sequence
        ([1], 0),                   # Single element
        ([2, 1], 1),                # Two elements
        ([5, 3, 4, 2], 2),          # Complex case
        ([1, 2, 3, 4], 0),          # Already sorted increasing
        ([4, 3, 2, 1], 3),          # Fully decreasing
        ([10, -5, 3], 1),           # With negative numbers
        ([1, 3, 2, 4], 1)           # One inversion
    ]
    
    approaches = [
        ("Simulation", solution.minOperations),
        ("Optimized", solution.minOperations_optimized),
        ("Verbose", solution.minOperations_verbose)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for nums, expected in test_cases:
            result = method(nums[:])  # Pass copy
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} nums={nums} → {result} (expected: {expected})")
            else:
                print(f"  {status} nums={nums} → {result}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed walkthrough for Example 1
    print("Detailed walkthrough for Example 1: nums=[5,2,3,1]")
    nums = [5, 2, 3, 1]
    
    print(f"Initial: {nums}")
    print(f"Is non-decreasing? {solution.is_non_decreasing(nums)}")
    print()
    
    operations = 0
    step = 1
    
    while not solution.is_non_decreasing(nums):
        print(f"Step {step}:")
        print(f"  Current array: {nums}")
        
        # Find all pairs and their sums
        print(f"  Adjacent pairs and sums:")
        pairs = []
        for i in range(len(nums) - 1):
            pair_sum = nums[i] + nums[i + 1]
            pairs.append((i, nums[i], nums[i + 1], pair_sum))
            marker = " ← minimum" if pair_sum == min(p[3] for p in pairs) else ""
            print(f"    Index {i}: ({nums[i]}, {nums[i+1]}) → sum = {pair_sum}{marker}")
        
        # Find minimum
        min_idx = min(pairs, key=lambda x: x[3])[0]
        print(f"  Merge pair at index {min_idx}: ({nums[min_idx]}, {nums[min_idx+1]})")
        
        # Merge
        new_val = nums[min_idx] + nums[min_idx + 1]
        nums[min_idx] = new_val
        nums.pop(min_idx + 1)
        operations += 1
        
        print(f"  After merge: {nums}")
        print(f"  Is non-decreasing? {solution.is_non_decreasing(nums)}")
        print()
        step += 1
    
    print(f"Final array: {nums}")
    print(f"Total operations: {operations}")
    print()
    
    print("Key Insights:")
    print("1. Always merge the pair with MINIMUM sum (counterintuitive but specified)")
    print("2. If multiple pairs have same minimum sum, choose leftmost")
    print("3. Keep merging until array becomes non-decreasing")
    print("4. Time complexity: O(n³) in worst case - n iterations × n to find min × n to check sorted")
    print("5. Space complexity: O(1) if modifying in-place, O(n) if creating copies")