# LeetCode 11: Container With Most Water

class Solution:
    # Approach 1: Brute Force - Check all pairs
    def maxArea_brute(self, height):
        n = len(height)
        max_water = 0
        
        # Check all possible pairs of lines
        for i in range(n):
            for j in range(i + 1, n):
                # Water level is determined by the shorter line
                water_level = min(height[i], height[j])
                # Width is the distance between the lines
                width = j - i
                # Area = height * width
                area = water_level * width
                max_water = max(max_water, area)
        
        return max_water
    
    # Approach 2: Two Pointers (Optimal)
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0
        
        # Use two pointers moving inward
        while left < right:
            # Calculate current area
            water_level = min(height[left], height[right])
            width = right - left
            current_area = water_level * width
            max_water = max(max_water, current_area)
            
            # Move the pointer with smaller height inward
            # This is the key insight: moving the taller pointer won't increase area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
    
    # Approach 3: Two Pointers with detailed explanation
    def maxArea_explained(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Current container dimensions
            left_height = height[left]
            right_height = height[right]
            width = right - left
            
            # Water level is limited by the shorter wall
            water_level = min(left_height, right_height)
            current_area = water_level * width
            
            # Update maximum
            if current_area > max_water:
                max_water = current_area
            
            # Greedy choice: move the pointer with smaller height
            # Why? Because keeping the smaller height and reducing width
            # will never give us a larger area
            if left_height < right_height:
                # Move left pointer to find potentially taller left wall
                left += 1
            elif right_height < left_height:
                # Move right pointer to find potentially taller right wall
                right -= 1
            else:
                # Heights are equal, move either pointer
                # Moving both would work too, but one is sufficient
                left += 1
        
        return max_water

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1, 2, 4, 3], 4),
        ([2, 3, 4, 5, 18, 17, 6], 17 * 4),  # height[4] * (6-4) = 72
        ([1, 8, 100, 2, 100, 4, 8, 3, 7], 200)  # 100 * 2 = 200
    ]
    
    print("Testing maxArea (Two Pointers - Optimal):")
    for heights, expected in test_cases:
        result = solution.maxArea(heights)
        status = "✓" if result == expected else "✗"
        print(f"{status} maxArea({heights}) = {result} (expected: {expected})")
    
    print("\nTesting maxArea_brute (Brute Force):")
    for heights, expected in test_cases:
        result = solution.maxArea_brute(heights)
        status = "✓" if result == expected else "✗"
        print(f"{status} maxArea_brute({heights}) = {result} (expected: {expected})")
    
    print("\nStep-by-step example with [1,8,6,2,5,4,8,3,7]:")
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    left, right = 0, len(heights) - 1
    step = 1
    max_area = 0
    
    while left < right:
        width = right - left
        water_level = min(heights[left], heights[right])
        area = water_level * width
        max_area = max(max_area, area)
        
        print(f"Step {step}: left={left}(h={heights[left]}), right={right}(h={heights[right]})")
        print(f"  Width={width}, WaterLevel={water_level}, Area={area}, MaxSoFar={max_area}")
        
        if heights[left] < heights[right]:
            left += 1
            print(f"  Move left pointer (smaller height)")
        else:
            right -= 1
            print(f"  Move right pointer (smaller/equal height)")
        
        step += 1
        if step > 10:  # Prevent too much output
            break
    
    print(f"\nFinal result: {max_area}")