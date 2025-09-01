# LeetCode 2270: Number of Ways to Split Array

class Solution:
    # Approach 1: Prefix Sum (Optimal)
    def waysToSplitArray(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        
        left_sum = 0
        valid_splits = 0
        
        # Check each possible split position (0 to n-2)
        for i in range(n - 1):  # i < n-1 ensures at least one element on right
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            
            # Check if left_sum >= right_sum
            if left_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits
    
    # Approach 2: Prefix Sum Array (Alternative)
    def waysToSplitArray_prefix_array(self, nums):
        n = len(nums)
        
        # Build prefix sum array
        prefix = [0] * (n + 1)  # prefix[i] = sum of nums[0:i]
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        valid_splits = 0
        total_sum = prefix[n]
        
        # Check each split position
        for i in range(n - 1):
            left_sum = prefix[i + 1]    # sum of nums[0:i+1]
            right_sum = total_sum - left_sum  # sum of nums[i+1:n]
            
            if left_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits
    
    # Approach 3: Brute Force (for understanding)
    def waysToSplitArray_brute(self, nums):
        n = len(nums)
        valid_splits = 0
        
        # Try each possible split position
        for i in range(n - 1):  # 0 <= i < n-1
            # Calculate left part sum: nums[0] to nums[i]
            left_sum = sum(nums[0:i+1])
            
            # Calculate right part sum: nums[i+1] to nums[n-1]  
            right_sum = sum(nums[i+1:n])
            
            # Check if valid split
            if left_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits
    
    # Approach 4: Mathematical Optimization
    def waysToSplitArray_math(self, nums):
        """
        Key insight: left_sum >= right_sum is equivalent to:
        left_sum >= total_sum - left_sum
        2 * left_sum >= total_sum
        left_sum >= total_sum / 2
        """
        n = len(nums)
        total_sum = sum(nums)
        
        left_sum = 0
        valid_splits = 0
        
        for i in range(n - 1):
            left_sum += nums[i]
            
            # Check if 2 * left_sum >= total_sum
            if 2 * left_sum >= total_sum:
                valid_splits += 1
        
        return valid_splits
    
    # Approach 5: Running difference (Creative approach)
    def waysToSplitArray_difference(self, nums):
        n = len(nums)
        
        # Calculate the difference: left_sum - right_sum
        # Initially, all elements are in right part
        difference = -sum(nums)
        valid_splits = 0
        
        for i in range(n - 1):
            # Move nums[i] from right to left
            # This increases difference by 2 * nums[i]
            difference += 2 * nums[i]
            
            # Valid split if difference >= 0 (left_sum >= right_sum)
            if difference >= 0:
                valid_splits += 1
        
        return valid_splits

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([10, 4, -8, 7], 2),    # Example 1
        ([2, 3, 1, 0], 2),      # Example 2
        ([1, 1], 1),            # Simple case
        ([0, 0], 1),            # All zeros
        ([-1, -2, -3], 0),      # All negative, decreasing
        ([5, -5], 1),           # Zero sum
        ([1, -1, 1, -1], 2),    # Alternating
        ([10, -5, -3, 2], 1),   # Mixed values
        ([1, 2, 3, 4, 5], 3),   # Increasing sequence
        ([-5, -4, -3, -2, -1], 0)  # All negative, increasing
    ]
    
    approaches = [
        ("Prefix Sum (Optimal)", solution.waysToSplitArray),
        ("Prefix Array", solution.waysToSplitArray_prefix_array),
        ("Mathematical", solution.waysToSplitArray_math),
        ("Running Difference", solution.waysToSplitArray_difference),
        ("Brute Force", solution.waysToSplitArray_brute)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for nums, expected in test_cases:
            result = method(nums)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} {nums} → {result} (expected: {expected})")
            else:
                print(f"  {status} {nums} → {result}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed step-by-step for Example 1: [10, 4, -8, 7]
    print("Step-by-step trace for [10, 4, -8, 7]:")
    nums = [10, 4, -8, 7]
    n = len(nums)
    total_sum = sum(nums)  # = 13
    
    print(f"Array: {nums}")
    print(f"Total sum: {total_sum}")
    print(f"Valid split positions: 0 to {n-2}")
    print()
    
    left_sum = 0
    valid_splits = 0
    
    for i in range(n - 1):
        left_sum += nums[i]
        right_sum = total_sum - left_sum
        is_valid = left_sum >= right_sum
        
        if is_valid:
            valid_splits += 1
        
        print(f"Split at index {i}:")
        print(f"  Left part:  {nums[:i+1]} → sum = {left_sum}")
        print(f"  Right part: {nums[i+1:]} → sum = {right_sum}")
        print(f"  Valid? {left_sum} >= {right_sum} → {is_valid}")
        print()
    
    print(f"Total valid splits: {valid_splits}")
    
    # Demonstrate mathematical optimization
    print("\nMathematical optimization explanation:")
    print("Instead of calculating right_sum = total_sum - left_sum,")
    print("we can check: left_sum >= right_sum")
    print("              left_sum >= total_sum - left_sum")
    print("              2 * left_sum >= total_sum")
    print("              left_sum >= total_sum / 2")
    print()
    
    left_sum = 0
    for i in range(n - 1):
        left_sum += nums[i] 
        threshold = total_sum / 2
        is_valid = left_sum >= threshold
        print(f"i={i}: left_sum={left_sum}, threshold={threshold:.1f}, valid={is_valid}")
    
    # Demonstrate running difference approach
    print("\nRunning difference explanation:")
    print("Track difference = left_sum - right_sum")
    print("Initially all elements in right: difference = -total_sum")
    print("Moving element from right to left increases difference by 2 * element")
    print()
    
    difference = -total_sum
    print(f"Initial difference: {difference}")
    
    for i in range(n - 1):
        difference += 2 * nums[i]
        is_valid = difference >= 0
        print(f"i={i}: move {nums[i]}, difference={difference}, valid={is_valid}")
    
    print("\nWhy running difference works:")
    print("- Moving element x from right to left:")
    print("  - Decreases right_sum by x")
    print("  - Increases left_sum by x") 
    print("  - Net change in (left_sum - right_sum) = +x - (-x) = +2x")