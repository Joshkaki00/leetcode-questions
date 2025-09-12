# LeetCode 88: Merge Sorted Array

class Solution:
    # Approach 1: Two pointers from the end (Optimal)
    def merge(self, nums1, m, nums2, n):
        """
        Merge nums2 into nums1 in-place.
        Key insight: Work backwards to avoid overwriting unprocessed elements.
        """
        # Pointers for nums1, nums2, and result position
        i = m - 1      # Last element in nums1's valid portion
        j = n - 1      # Last element in nums2
        k = m + n - 1  # Last position in nums1 (where we place elements)
        
        # Merge from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If nums2 has remaining elements, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
        # Note: if nums1 has remaining elements, they're already in place
    
    # Approach 2: Using extra space (not optimal but educational)
    def merge_extra_space(self, nums1, m, nums2, n):
        """
        Create a copy and merge - easier to understand but uses O(m) extra space
        """
        # Make a copy of the valid portion of nums1
        nums1_copy = nums1[:m]
        
        # Two pointers for merging
        i = j = 0
        
        # Merge into nums1
        for k in range(m + n):
            if i < m and (j >= n or nums1_copy[i] <= nums2[j]):
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
    
    # Approach 3: Forward merging with shifting (inefficient)
    def merge_forward_shift(self, nums1, m, nums2, n):
        """
        Insert elements from nums2 into nums1 in forward direction.
        Requires shifting elements, making it O((m+n)^2) time.
        """
        j = 0  # Pointer for nums2
        
        for i in range(n):
            # Find insertion position for nums2[j] in nums1
            insert_pos = 0
            while insert_pos < m + i and nums1[insert_pos] < nums2[j]:
                insert_pos += 1
            
            # Shift elements to the right
            for shift in range(m + i, insert_pos, -1):
                nums1[shift] = nums1[shift - 1]
            
            # Insert nums2[j]
            nums1[insert_pos] = nums2[j]
            j += 1
    
    # Approach 4: Built-in sort (not optimal but works)
    def merge_builtin_sort(self, nums1, m, nums2, n):
        """
        Place all elements and sort - O((m+n)log(m+n)) time
        """
        # Copy nums2 elements into the end of nums1
        for i in range(n):
            nums1[m + i] = nums2[i]
        
        # Sort the entire array
        nums1.sort()

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    def test_merge(method, nums1, m, nums2, n, expected):
        # Make copies since we modify in-place
        test_nums1 = nums1.copy()
        test_nums2 = nums2.copy()
        
        method(test_nums1, m, test_nums2, n)
        return test_nums1 == expected
    
    test_cases = [
        # (nums1, m, nums2, n, expected)
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),  # Example 1
        ([1], 1, [], 0, [1]),                            # Example 2
        ([0], 0, [1], 1, [1]),                           # Example 3
        ([2,0], 1, [1], 1, [1,2]),                       # Simple case
        ([1,2,4,5,0,0,0], 4, [3,6,7], 3, [1,2,3,4,5,6,7]), # No overlap
        ([4,5,6,0,0,0], 3, [1,2,3], 3, [1,2,3,4,5,6]),   # nums2 all smaller
        ([1,2,3,0,0,0], 3, [4,5,6], 3, [1,2,3,4,5,6]),   # nums2 all larger
        ([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3, [-1,0,0,1,2,2,3,3,3]) # Negative numbers
    ]
    
    approaches = [
        ("Two Pointers (Optimal)", solution.merge),
        ("Extra Space", solution.merge_extra_space),
        ("Built-in Sort", solution.merge_builtin_sort)
        # Note: Forward shift approach is too slow, commented out
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for nums1, m, nums2, n, expected in test_cases:
            result = test_merge(method, nums1, m, nums2, n, expected)
            status = "✓" if result else "✗"
            
            if not result:
                all_correct = False
                # Show the actual result for debugging
                test_nums1 = nums1.copy()
                method(test_nums1, m, nums2.copy(), n)
                print(f"  {status} nums1={nums1[:m]}, nums2={nums2} → {test_nums1} (expected: {expected})")
            else:
                print(f"  {status} nums1={nums1[:m]}, nums2={nums2} → {expected}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed trace for Example 1
    print("Detailed trace for Example 1: nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3")
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3
    
    print(f"Initial: nums1={nums1}, nums2={nums2}")
    print("Working backwards to avoid overwriting:")
    
    i, j, k = m - 1, n - 1, m + n - 1
    
    step = 1
    while i >= 0 and j >= 0:
        print(f"Step {step}: comparing nums1[{i}]={nums1[i]} vs nums2[{j}]={nums2[j]}")
        
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            print(f"  nums1[{i}] > nums2[{j}], place {nums1[i]} at position {k}")
            i -= 1
        else:
            nums1[k] = nums2[j]
            print(f"  nums1[{i}] <= nums2[{j}], place {nums2[j]} at position {k}")
            j -= 1
        
        k -= 1
        print(f"  Result so far: {nums1}")
        step += 1
    
    # Handle remaining elements
    while j >= 0:
        nums1[k] = nums2[j]
        print(f"Remaining nums2[{j}]={nums2[j]} placed at position {k}")
        j -= 1
        k -= 1
    
    print(f"Final result: {nums1}")
    
    print("\nAlgorithm advantages:")
    print("- O(m + n) time complexity - optimal")
    print("- O(1) extra space - in-place modification")
    print("- Works backwards to avoid overwriting unprocessed elements")
    print("- Handles all edge cases (empty arrays, all elements from one array, etc.)")
    
    print("\nWhy working backwards is crucial:")
    print("- nums1 has extra space at the end")
    print("- Largest elements should go at the end")
    print("- Working forward would overwrite elements we haven't processed yet")
    print("- Working backward ensures we never overwrite needed data")