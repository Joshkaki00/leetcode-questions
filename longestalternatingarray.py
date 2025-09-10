# LeetCode 2765: Longest Alternating Subarray

class Solution:
    # Approach 1: Single pass with state tracking (Optimal)
    def alternatingSubarray(self, nums):
        n = len(nums)
        max_length = -1
        
        i = 0
        while i < n - 1:
            # Check if we can start an alternating subarray at position i
            if nums[i + 1] == nums[i] + 1:
                # Found potential start: nums[i], nums[i+1] = s0, s1
                length = 2
                j = i + 1
                
                # Extend the alternating pattern
                while j < n - 1:
                    expected_diff = -1 if length % 2 == 0 else 1
                    if nums[j + 1] == nums[j] + expected_diff:
                        length += 1
                        j += 1
                    else:
                        break
                
                max_length = max(max_length, length)
                
                # Move to next potential start
                # Key optimization: if we found pattern of length k starting at i,
                # next pattern can't start before i + k - 1
                i = j
            else:
                i += 1
        
        return max_length
    
    # Approach 2: Brute force - check all possible starting positions
    def alternatingSubarray_brute(self, nums):
        n = len(nums)
        max_length = -1
        
        # Try each starting position
        for i in range(n - 1):
            # Check if alternating pattern can start at i
            if nums[i + 1] != nums[i] + 1:
                continue
            
            # Extend the alternating pattern from position i
            length = 2
            for j in range(i + 2, n):
                expected_diff = -1 if (j - i) % 2 == 0 else 1
                if nums[j] == nums[j - 1] + expected_diff:
                    length += 1
                else:
                    break
            
            max_length = max(max_length, length)
        
        return max_length
    
    # Approach 3: Helper function for clarity
    def alternatingSubarray_helper(self, nums):
        def is_valid_alternating(start, end):
            """Check if subarray from start to end follows alternating pattern"""
            if end - start + 1 < 2:
                return False
            
            # First two elements must be consecutive
            if nums[start + 1] != nums[start] + 1:
                return False
            
            # Check alternating pattern
            for i in range(start + 2, end + 1):
                pos_in_pattern = i - start
                expected_diff = -1 if pos_in_pattern % 2 == 0 else 1
                if nums[i] != nums[i - 1] + expected_diff:
                    return False
            
            return True
        
        n = len(nums)
        max_length = -1
        
        # Check all possible subarrays
        for start in range(n):
            for end in range(start + 1, n):
                if is_valid_alternating(start, end):
                    max_length = max(max_length, end - start + 1)
        
        return max_length
    
    # Approach 4: Pattern-based with explicit state
    def alternatingSubarray_state(self, nums):
        n = len(nums)
        max_length = -1
        
        i = 0
        while i < n - 1:
            # Look for start of alternating pattern
            if nums[i + 1] == nums[i] + 1:
                start = i
                current_length = 2
                expected_next = nums[i] # Next should be nums[i] again
                
                # Extend pattern
                j = i + 2
                while j < n:
                    if nums[j] == expected_next:
                        current_length += 1
                        # Toggle expected value for next iteration
                        expected_next = nums[i] if expected_next == nums[i] + 1 else nums[i] + 1
                        j += 1
                    else:
                        break
                
                max_length = max(max_length, current_length)
                i = start + 1  # Move to next potential starting position
            else:
                i += 1
        
        return max_length

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([2, 3, 4, 3, 4], 4),        # Example 1: [3,4,3,4]
        ([4, 5, 6], 2),              # Example 2: [4,5] or [5,6]
        ([1, 2, 1, 2, 1], 5),        # Perfect alternating
        ([1, 2, 3, 4], 2),           # Multiple length-2 patterns
        ([1, 3, 2, 4], -1),          # No valid alternating subarray
        ([2, 3, 2, 3, 2, 3], 6),     # Long alternating pattern
        ([5, 6, 5], 3),              # Simple 3-element pattern
        ([1, 2, 1, 3, 4, 3, 4, 3], 4), # [3,4,3,4] in the end
        ([10, 11, 10, 11], 4),       # Full array is alternating
        ([7, 8, 9, 8, 9], 4),        # [8,9,8,9]
        ([1, 1, 2, 1], 3),           # [1,2,1] starting from index 1
        ([3, 4, 5, 4, 5, 4], 5)      # [4,5,4,5,4]
    ]
    
    approaches = [
        ("Optimal Single Pass", solution.alternatingSubarray),
        ("Brute Force", solution.alternatingSubarray_brute),
        ("Helper Function", solution.alternatingSubarray_helper),
        ("State-based", solution.alternatingSubarray_state)
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
    
    # Detailed trace for Example 1: [2,3,4,3,4]
    print("Detailed trace for [2,3,4,3,4]:")
    nums = [2, 3, 4, 3, 4]
    n = len(nums)
    
    print(f"Array: {nums}")
    print("Looking for alternating subarrays where s[1] = s[0] + 1")
    print("Pattern: [s0, s0+1, s0, s0+1, s0, ...]")
    print()
    
    # Find all valid alternating subarrays
    valid_subarrays = []
    
    for start in range(n - 1):
        if nums[start + 1] == nums[start] + 1:
            # Found potential start
            end = start + 1
            s0, s1 = nums[start], nums[start + 1]
            
            # Extend as far as possible
            while end + 1 < n:
                pos_in_pattern = (end + 1) - start
                expected = s0 if pos_in_pattern % 2 == 0 else s1
                if nums[end + 1] == expected:
                    end += 1
                else:
                    break
            
            if end > start:  # At least length 2
                subarray = nums[start:end+1]
                valid_subarrays.append((start, end, subarray))
    
    print("Valid alternating subarrays found:")
    for start, end, subarray in valid_subarrays:
        print(f"  indices {start}-{end}: {subarray} (length {len(subarray)})")
    
    if valid_subarrays:
        max_len = max(len(subarray) for _, _, subarray in valid_subarrays)
        print(f"\nMaximum length: {max_len}")
    else:
        print("\nNo valid alternating subarrays found")
    
    # Show pattern verification for [3,4,3,4]
    print("\nPattern verification for [3,4,3,4]:")
    test_array = [3, 4, 3, 4]
    s0, s1 = test_array[0], test_array[1]
    print(f"s0 = {s0}, s1 = {s1}")
    print(f"s1 - s0 = {s1 - s0} (should be 1) ✓")
    
    for i in range(2, len(test_array)):
        expected = s0 if i % 2 == 0 else s1
        actual = test_array[i]
        diff = actual - test_array[i-1]
        expected_diff = -1 if i % 2 == 0 else 1
        print(f"Position {i}: expected {expected}, got {actual}, diff = {diff} (should be {expected_diff}) {'✓' if actual == expected else '✗'}")
    
    print("\nKey insights:")
    print("- Pattern must start with consecutive integers (s0, s0+1)")
    print("- Then alternates between those two values")
    print("- Differences follow pattern: +1, -1, +1, -1, ...")
    print("- We need at least length 2 for a valid alternating subarray")