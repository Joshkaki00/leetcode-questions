# LeetCode 3423: Maximum Difference Between Adjacent Elements in a Circular Array

# SCENARIO: Temperature Monitoring System for Climate Control
# You're developing a smart building climate control system that monitors temperature
# sensors arranged in a circular pattern around a large conference room. Each sensor
# reports the temperature at its location, and the system needs to identify the
# maximum temperature difference between any two adjacent sensors to detect potential
# HVAC malfunctions or hot/cold spots. Since the sensors form a complete circle around
# the room, the first and last sensors are also adjacent to each other. Large temperature
# differences between adjacent sensors indicate poor air circulation or equipment issues
# that need immediate attention. Your algorithm helps facilities management quickly
# identify problem areas before they affect occupant comfort or energy efficiency.

class Solution:
    # Approach 1: Single Pass with Circular Check (Optimal)
    def maxAdjacentDistance(self, nums):
        """
        Check all adjacent pairs including the wrap-around from last to first.
        """
        n = len(nums)
        max_diff = 0
        
        # Check all adjacent pairs (including circular)
        for i in range(n):
            # Next index with wrap-around
            next_idx = (i + 1) % n
            
            # Calculate absolute difference
            diff = abs(nums[i] - nums[next_idx])
            
            # Update maximum
            max_diff = max(max_diff, diff)
        
        return max_diff
    
    # Approach 2: Explicit Circular Handling
    def maxAdjacentDistance_explicit(self, nums):
        """
        Check regular pairs separately, then check wrap-around pair.
        """
        n = len(nums)
        max_diff = 0
        
        # Check all consecutive pairs (not including wrap-around)
        for i in range(n - 1):
            diff = abs(nums[i] - nums[i + 1])
            max_diff = max(max_diff, diff)
        
        # Check wrap-around pair (last and first elements)
        wrap_diff = abs(nums[n - 1] - nums[0])
        max_diff = max(max_diff, wrap_diff)
        
        return max_diff
    
    # Approach 3: List Comprehension (Pythonic)
    def maxAdjacentDistance_comprehension(self, nums):
        """
        Use list comprehension to generate all differences at once.
        """
        n = len(nums)
        
        # Generate all adjacent differences including circular
        differences = [abs(nums[i] - nums[(i + 1) % n]) for i in range(n)]
        
        return max(differences)
    
    # Approach 4: With Detailed Tracking (Educational)
    def maxAdjacentDistance_verbose(self, nums):
        """
        Track which pair has maximum difference for debugging/visualization.
        """
        n = len(nums)
        max_diff = 0
        max_pair = None
        
        for i in range(n):
            next_idx = (i + 1) % n
            diff = abs(nums[i] - nums[next_idx])
            
            if diff > max_diff:
                max_diff = diff
                max_pair = (i, next_idx, nums[i], nums[next_idx])
        
        return max_diff

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1, 2, 4], 3),              # Example 1: |4-1|=3 (circular)
        ([-5, -10, -5], 5),          # Example 2: |-5-(-10)|=5
        ([1, 1, 1], 0),              # All same
        ([1, 100], 99),              # Two elements
        ([5, 3, 8, 1], 7),           # Max is |8-1|=7
        ([10, 20, 15, 25], 10),      # Multiple differences
        ([-50, 50], 100),            # Large negative to positive
        ([0, 0, 0, 0], 0),           # All zeros
        ([7, 2, 9, 1, 5], 8),        # |9-1|=8
        ([100, 1, 99], 99)           # |100-1|=99 circular
    ]
    
    approaches = [
        ("Single Pass Modulo", solution.maxAdjacentDistance),
        ("Explicit Circular", solution.maxAdjacentDistance_explicit),
        ("List Comprehension", solution.maxAdjacentDistance_comprehension),
        ("Verbose Tracking", solution.maxAdjacentDistance_verbose)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for nums, expected in test_cases:
            result = method(nums)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} nums={nums} → {result} (expected: {expected})")
            else:
                print(f"  {status} nums={nums} → {result}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed walkthrough for Example 1
    print("Detailed walkthrough for Example 1: nums=[1,2,4]")
    nums = [1, 2, 4]
    n = len(nums)
    
    print(f"Array: {nums}")
    print(f"Length: {n}")
    print()
    print("Circular array visualization:")
    print("    [0]=1")
    print("   /      \\")
    print("[2]=4 ---- [1]=2")
    print()
    
    print("Checking all adjacent pairs:")
    max_diff = 0
    
    for i in range(n):
        next_idx = (i + 1) % n
        diff = abs(nums[i] - nums[next_idx])
        
        print(f"Pair {i}: nums[{i}]={nums[i]} and nums[{next_idx}]={nums[next_idx]}")
        print(f"  Difference: |{nums[i]} - {nums[next_idx]}| = {diff}")
        
        if diff > max_diff:
            max_diff = diff
            print(f"  New maximum! ★")
        print()
    
    print(f"Maximum difference: {max_diff}")
    print()
    
    # Detailed walkthrough for Example 2
    print("Detailed walkthrough for Example 2: nums=[-5,-10,-5]")
    nums = [-5, -10, -5]
    n = len(nums)
    
    print(f"Array: {nums}")
    print()
    print("Checking all adjacent pairs:")
    
    for i in range(n):
        next_idx = (i + 1) % n
        diff = abs(nums[i] - nums[next_idx])
        
        is_circular = "← circular" if next_idx == 0 and i == n-1 else ""
        print(f"Pair {i}: nums[{i}]={nums[i]:3d} and nums[{next_idx}]={nums[next_idx]:3d} {is_circular}")
        print(f"  |{nums[i]:3d} - {nums[next_idx]:3d}| = {diff}")
    
    print()
    print("Key Insights:")
    print("1. Circular array means first and last elements are adjacent")
    print("2. Use modulo (%) to handle wrap-around: (i+1) % n")
    print("3. Must check ALL n pairs, not just n-1 pairs")
    print("4. Time complexity: O(n) - single pass through array")
    print("5. Space complexity: O(1) - only tracking maximum")