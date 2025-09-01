# LeetCode 1567: Maximum Length of Subarray With Positive Product

class Solution:
    # Approach 1: Dynamic Programming (Optimal)
    def getMaxLen(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        # pos: length of longest subarray ending at current index with positive product
        # neg: length of longest subarray ending at current index with negative product
        pos = neg = 0
        max_length = 0
        
        for num in nums:
            if num == 0:
                # Zero resets everything
                pos = neg = 0
            elif num > 0:
                # Positive number: extends both positive and negative subarrays
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            else:  # num < 0
                # Negative number: swaps positive and negative lengths
                new_pos = neg + 1 if neg > 0 else 0
                new_neg = pos + 1
                pos, neg = new_pos, new_neg
            
            max_length = max(max_length, pos)
        
        return max_length
    
    # Approach 2: Track negative count (Alternative DP)
    def getMaxLen_negCount(self, nums):
        n = len(nums)
        max_length = 0
        
        # Split array by zeros and process each segment
        start = 0
        for i in range(n + 1):
            if i == n or nums[i] == 0:
                # Process segment from start to i-1
                if i > start:
                    segment_length = self.max_positive_length(nums[start:i])
                    max_length = max(max_length, segment_length)
                start = i + 1
        
        return max_length
    
    def max_positive_length(self, segment):
        """Find max length with positive product in segment without zeros"""
        if not segment:
            return 0
        
        n = len(segment)
        negative_count = sum(1 for x in segment if x < 0)
        
        # If even number of negatives, whole segment has positive product
        if negative_count % 2 == 0:
            return n
        
        # If odd number of negatives, we need to exclude one negative
        # Try excluding first negative or last negative
        first_neg = next(i for i in range(n) if segment[i] < 0)
        last_neg = next(i for i in range(n-1, -1, -1) if segment[i] < 0)
        
        # Exclude first negative: take segment[first_neg+1:]
        # Exclude last negative: take segment[:last_neg]
        option1 = n - first_neg - 1  # Length after first negative
        option2 = last_neg  # Length before last negative
        
        return max(option1, option2)
    
    # Approach 3: Brute Force with Optimization (for understanding)
    def getMaxLen_brute(self, nums):
        n = len(nums)
        max_length = 0
        
        for i in range(n):
            if nums[i] == 0:
                continue
            
            negative_count = 0
            for j in range(i, n):
                if nums[j] == 0:
                    break
                
                if nums[j] < 0:
                    negative_count += 1
                
                # Product is positive if even number of negatives
                if negative_count % 2 == 0:
                    max_length = max(max_length, j - i + 1)
        
        return max_length
    
    # Approach 4: Two-pass approach (intuitive)
    def getMaxLen_twopass(self, nums):
        """
        Key insight: In a segment without zeros, if we have odd number of negatives,
        we must exclude either the first or the last negative to get positive product.
        """
        n = len(nums)
        max_length = 0
        
        # Forward pass: track length from start to current position
        pos_len = neg_len = 0
        for i in range(n):
            if nums[i] == 0:
                pos_len = neg_len = 0
            elif nums[i] > 0:
                pos_len += 1
                neg_len = neg_len + 1 if neg_len > 0 else 0
            else:  # nums[i] < 0
                temp = pos_len
                pos_len = neg_len + 1 if neg_len > 0 else 0
                neg_len = temp + 1
            
            max_length = max(max_length, pos_len)
        
        return max_length

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1, -2, -3, 4], 4),          # Example 1: whole array
        ([0, 1, -2, -3, -4], 3),     # Example 2: [1,-2,-3]
        ([-1, -2, -3, 0, 1], 2),     # Example 3: [-1,-2] or [-2,-3]
        ([1, 2, 3, 4], 4),           # All positive
        ([-1, -2, -3, -4], 4),       # Even number of negatives
        ([-1, -2, -3], 2),           # Odd negatives: exclude first or last
        ([0], 0),                    # Single zero
        ([5], 1),                    # Single positive
        ([-5], 0),                   # Single negative
        ([1, -2, 0, -3, 4], 1),      # Multiple segments
        ([-1, 0, -2, -3, 0, 4], 2),  # Multiple zeros
        ([0, 0, 0], 0),              # All zeros
        ([1, 0, -1, 0, 2], 1),       # Alternating with zeros
        ([-1, -1, -1, -1, -1], 4)    # 5 negatives: max is 4 (exclude one)
    ]
    
    approaches = [
        ("Dynamic Programming (Optimal)", solution.getMaxLen),
        ("Negative Count", solution.getMaxLen_negCount),
        ("Brute Force", solution.getMaxLen_brute),
        ("Two Pass", solution.getMaxLen_twopass)
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
    
    # Step-by-step trace for Example 1: [1,-2,-3,4]
    print("Step-by-step trace for [1,-2,-3,4]:")
    nums = [1, -2, -3, 4]
    pos = neg = 0
    max_length = 0
    
    for i, num in enumerate(nums):
        old_pos, old_neg = pos, neg
        
        if num == 0:
            pos = neg = 0
        elif num > 0:
            pos += 1
            neg = neg + 1 if neg > 0 else 0
        else:  # num < 0
            new_pos = neg + 1 if neg > 0 else 0
            new_neg = pos + 1
            pos, neg = new_pos, new_neg
        
        max_length = max(max_length, pos)
        
        print(f"  i={i}, num={num}: pos {old_pos}→{pos}, neg {old_neg}→{neg}, max_len={max_length}")
    
    print(f"  Final result: {max_length}")
    
    # Explanation of why this works
    print("\nWhy the algorithm works:")
    print("- pos: length of longest subarray ending here with POSITIVE product")
    print("- neg: length of longest subarray ending here with NEGATIVE product") 
    print("- When we see a positive number: extends both subarrays")
    print("- When we see a negative number: swaps pos/neg (negative * negative = positive)")
    print("- When we see zero: resets everything (can't include zero in positive product)")