# LeetCode 1005: Maximize Sum Of Array After K Negations

# SCENARIO: Financial Portfolio Optimization
# You're a financial analyst managing an investment portfolio with various assets.
# Some positions are showing losses (negative values) while others show gains (positive values).
# You have exactly K opportunities to "hedge" positions by reversing their sign 
# (converting losses to gains or vice versa). Your hedging budget requires you to use
# exactly K hedges - no more, no less. You can hedge the same position multiple times
# if needed. Your goal is to maximize the total portfolio value. This requires strategic
# thinking: prioritize converting the biggest losses to gains first, but what happens
# when you run out of losses? The company's quarterly performance depends on your 
# optimization strategy.

class Solution:
    # Approach 1: Greedy with Sorting (Optimal)
    def largestSumAfterKNegations(self, nums, k):
        """
        Strategy: Always flip the most negative number to maximize sum.
        If we run out of negatives, flip the smallest absolute value back and forth.
        """
        # Sort to process most negative numbers first
        nums.sort()
        
        # Phase 1: Flip negative numbers (biggest negative first)
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        
        # Phase 2: If k is still positive
        # If k is even, flips cancel out - do nothing
        # If k is odd, flip the smallest absolute value
        if k % 2 == 1:
            nums.sort()  # Re-sort to find smallest absolute value
            nums[0] = -nums[0]
        
        return sum(nums)
    
    # Approach 2: Greedy with Min Heap (More Efficient)
    def largestSumAfterKNegations_heap(self, nums, k):
        """
        Use min heap to always access the smallest element efficiently.
        Avoids repeated sorting.
        """
        import heapq
        
        # Convert to min heap
        heapq.heapify(nums)
        
        # Perform k negations
        for _ in range(k):
            # Pop smallest element
            smallest = heapq.heappop(nums)
            # Flip it and push back
            heapq.heappush(nums, -smallest)
        
        return sum(nums)
    
    # Approach 3: Greedy with Absolute Value Tracking
    def largestSumAfterKNegations_tracking(self, nums, k):
        """
        Track negatives separately and handle remaining flips strategically.
        """
        # Sort by value
        nums.sort()
        
        # Count and flip negatives
        i = 0
        while i < len(nums) and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        
        # After flipping negatives, handle remaining k
        # Find minimum absolute value in array
        min_abs = min(abs(x) for x in nums)
        
        # If k is odd, we need to flip the smallest value
        if k % 2 == 1:
            # Subtract it twice (once to remove, once to add negative)
            return sum(nums) - 2 * min_abs
        
        return sum(nums)
    
    # Approach 4: Brute Force with Recursion (Educational - Too Slow)
    def largestSumAfterKNegations_brute(self, nums, k):
        """
        Try all possible combinations of k negations.
        Exponential time - only for understanding the problem.
        """
        def helper(arr, flips_left):
            if flips_left == 0:
                return sum(arr)
            
            max_sum = float('-inf')
            
            # Try flipping each index
            for i in range(len(arr)):
                arr[i] = -arr[i]  # Flip
                max_sum = max(max_sum, helper(arr, flips_left - 1))
                arr[i] = -arr[i]  # Unflip (backtrack)
            
            return max_sum
        
        return helper(nums[:], k)  # Pass copy to avoid modifying original

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([4, 2, 3], 1, 5),              # Example 1: flip smallest positive
        ([3, -1, 0, 2], 3, 6),          # Example 2: flip negative, then 0 twice
        ([2, -3, -1, 5, -4], 2, 13),    # Example 3: flip two largest negatives
        ([-8, 3, -5, -3, -5], 6, 22),   # Multiple negatives, even k
        ([-4, -2, -3], 4, 9),           # All negative, one extra flip
        ([1], 1, -1),                   # Single element, must flip
        ([5, 6, 9, -3, -4], 2, 27),     # Flip both negatives
        ([-2, 5, 0, 2, -2], 3, 11),     # Include zero
        ([1, 2, 3], 3, 3),              # All positive, odd k
        ([1, 2, 3], 2, 6)               # All positive, even k
    ]
    
    approaches = [
        ("Greedy with Sorting", solution.largestSumAfterKNegations),
        ("Min Heap", solution.largestSumAfterKNegations_heap),
        ("Absolute Value Tracking", solution.largestSumAfterKNegations_tracking)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for nums, k, expected in test_cases:
            result = method(nums[:], k)  # Pass copy
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} nums={nums}, k={k} → {result} (expected: {expected})")
            else:
                print(f"  {status} nums={nums}, k={k} → {result}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed walkthrough for Example 3
    print("Detailed walkthrough for Example 3: nums=[2,-3,-1,5,-4], k=2")
    nums = [2, -3, -1, 5, -4]
    k = 2
    
    print(f"Initial array: {nums}")
    print(f"k = {k} flips available")
    print()
    
    # Step-by-step greedy strategy
    print("Greedy Strategy: Flip most negative values first")
    nums_sorted = sorted(nums)
    print(f"Sorted array: {nums_sorted}")
    print()
    
    flips_used = 0
    for i in range(len(nums_sorted)):
        if flips_used < k and nums_sorted[i] < 0:
            old_val = nums_sorted[i]
            nums_sorted[i] = -nums_sorted[i]
            flips_used += 1
            print(f"Flip {flips_used}: {old_val} → {nums_sorted[i]}")
            print(f"  Current array: {nums_sorted}, sum = {sum(nums_sorted)}")
    
    print()
    remaining_k = k - flips_used
    print(f"After flipping negatives: {nums_sorted}")
    print(f"Remaining flips: {remaining_k}")
    
    if remaining_k > 0:
        if remaining_k % 2 == 1:
            min_val = min(nums_sorted)
            print(f"Odd remaining flips: flip smallest value {min_val}")
            print(f"Final sum = {sum(nums_sorted)} - 2*{min_val} = {sum(nums_sorted) - 2*min_val}")
        else:
            print(f"Even remaining flips: they cancel out")
            print(f"Final sum = {sum(nums_sorted)}")
    else:
        print(f"All flips used on negatives")
        print(f"Final sum = {sum(nums_sorted)}")
    
    print()
    print("Key Insights:")
    print("1. Greedy approach: always flip the most negative number")
    print("2. After negatives exhausted, even k's cancel out")
    print("3. Odd remaining k: flip smallest absolute value")
    print("4. Can flip same index multiple times (important for remaining k)")