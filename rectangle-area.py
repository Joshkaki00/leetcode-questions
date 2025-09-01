# LeetCode 223: Rectangle Area

class Solution:
    # Approach 1: Mathematical Formula (Optimal)
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        # Calculate individual rectangle areas
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # Calculate overlap area
        overlap_area = self.get_overlap_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        
        # Total area = sum of individual areas - overlap area
        return area_a + area_b - overlap_area
    
    def get_overlap_area(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """Calculate the area of overlap between two rectangles"""
        # Find overlap boundaries
        overlap_left = max(ax1, bx1)
        overlap_right = min(ax2, bx2)
        overlap_bottom = max(ay1, by1)
        overlap_top = min(ay2, by2)
        
        # Check if there's actual overlap
        if overlap_left >= overlap_right or overlap_bottom >= overlap_top:
            return 0  # No overlap
        
        # Calculate overlap area
        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_top - overlap_bottom
        return overlap_width * overlap_height
    
    # Approach 2: Step-by-step with clear variable names
    def computeArea_verbose(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        # Rectangle A dimensions
        width_a = ax2 - ax1
        height_a = ay2 - ay1
        area_a = width_a * height_a
        
        # Rectangle B dimensions  
        width_b = bx2 - bx1
        height_b = by2 - by1
        area_b = width_b * height_b
        
        # Find overlap region
        # Overlap exists only if rectangles intersect in both x and y directions
        x_overlap_start = max(ax1, bx1)
        x_overlap_end = min(ax2, bx2)
        y_overlap_start = max(ay1, by1)
        y_overlap_end = min(ay2, by2)
        
        # Calculate overlap area
        overlap_area = 0
        if x_overlap_start < x_overlap_end and y_overlap_start < y_overlap_end:
            overlap_width = x_overlap_end - x_overlap_start
            overlap_height = y_overlap_end - y_overlap_start
            overlap_area = overlap_width * overlap_height
        
        return area_a + area_b - overlap_area
    
    # Approach 3: Using helper functions for clarity
    def computeArea_modular(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        def rectangle_area(x1, y1, x2, y2):
            return (x2 - x1) * (y2 - y1)
        
        def rectangles_overlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
            return not (ax2 <= bx1 or bx2 <= ax1 or ay2 <= by1 or by2 <= ay1)
        
        def overlap_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
            if not rectangles_overlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
                return 0
            
            left = max(ax1, bx1)
            right = min(ax2, bx2)
            bottom = max(ay1, by1)
            top = min(ay2, by2)
            
            return (right - left) * (top - bottom)
        
        area_a = rectangle_area(ax1, ay1, ax2, ay2)
        area_b = rectangle_area(bx1, by1, bx2, by2)
        overlap = overlap_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        
        return area_a + area_b - overlap
    
    # Approach 4: Edge case handling with explicit checks
    def computeArea_safe(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        # Validate input rectangles (should have positive area)
        if ax1 >= ax2 or ay1 >= ay2 or bx1 >= bx2 or by1 >= by2:
            # Handle degenerate rectangles (lines or points)
            area_a = max(0, (ax2 - ax1) * (ay2 - ay1))
            area_b = max(0, (bx2 - bx1) * (by2 - by1))
            return area_a + area_b
        
        # Calculate areas
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # Check for overlap
        overlap_left = max(ax1, bx1)
        overlap_right = min(ax2, bx2)
        overlap_bottom = max(ay1, by1)
        overlap_top = min(ay2, by2)
        
        overlap_area = 0
        if overlap_left < overlap_right and overlap_bottom < overlap_top:
            overlap_area = (overlap_right - overlap_left) * (overlap_top - overlap_bottom)
        
        return area_a + area_b - overlap_area

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # Example 1: From the image
        (-3, 0, 3, 4, 0, -1, 9, 2, 45),
        
        # Example 2: Identical rectangles
        (-2, -2, 2, 2, -2, -2, 2, 2, 16),
        
        # No overlap
        (0, 0, 2, 2, 3, 3, 5, 5, 8),
        
        # Complete overlap (A inside B)
        (1, 1, 2, 2, 0, 0, 3, 3, 9),
        
        # Partial overlap
        (0, 0, 3, 3, 2, 2, 5, 5, 18),  # 9 + 9 - 0 = 18 (1x1 overlap)
        
        # Adjacent rectangles (touching but not overlapping)
        (0, 0, 2, 2, 2, 0, 4, 2, 8),
        
        # One rectangle is a line (degenerate case)
        (0, 0, 0, 2, 1, 1, 2, 2, 1),
        
        # Negative coordinates
        (-5, -5, -2, -2, -4, -4, -1, -1, 18),  # 9 + 9 - 0 = 18 (no overlap)
        
        # Complex overlap
        (0, 0, 4, 4, 2, 2, 6, 6, 32)  # 16 + 16 - 0 = 32 (2x2 overlap = 4, so 16+16-4=28, wait let me recalculate...)
    ]
    
    # Fix the last test case calculation
    test_cases[-1] = (0, 0, 4, 4, 2, 2, 6, 6, 28)  # 16 + 16 - 4 = 28
    
    approaches = [
        ("Mathematical (Optimal)", solution.computeArea),
        ("Verbose", solution.computeArea_verbose),
        ("Modular", solution.computeArea_modular),
        ("Safe", solution.computeArea_safe)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for *coords, expected in test_cases:
            ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = coords
            result = method(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} A({ax1},{ay1},{ax2},{ay2}) B({bx1},{by1},{bx2},{by2}) → {result} (expected: {expected})")
            else:
                print(f"  {status} A({ax1},{ay1},{ax2},{ay2}) B({bx1},{by1},{bx2},{by2}) → {result}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed walkthrough for Example 1
    print("Detailed walkthrough for Example 1:")
    ax1, ay1, ax2, ay2 = -3, 0, 3, 4
    bx1, by1, bx2, by2 = 0, -1, 9, 2
    
    print(f"Rectangle A: bottom-left({ax1},{ay1}) to top-right({ax2},{ay2})")
    print(f"Rectangle B: bottom-left({bx1},{by1}) to top-right({bx2},{by2})")
    print()
    
    # Calculate areas
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)
    print(f"Area A = ({ax2}-{ax1}) × ({ay2}-{ay1}) = {ax2-ax1} × {ay2-ay1} = {area_a}")
    print(f"Area B = ({bx2}-{bx1}) × ({by2}-{by1}) = {bx2-bx1} × {by2-by1} = {area_b}")
    print()
    
    # Calculate overlap
    overlap_left = max(ax1, bx1)
    overlap_right = min(ax2, bx2)
    overlap_bottom = max(ay1, by1)
    overlap_top = min(ay2, by2)
    
    print(f"Overlap boundaries:")
    print(f"  Left = max({ax1}, {bx1}) = {overlap_left}")
    print(f"  Right = min({ax2}, {bx2}) = {overlap_right}")
    print(f"  Bottom = max({ay1}, {by1}) = {overlap_bottom}")
    print(f"  Top = min({ay2}, {by2}) = {overlap_top}")
    print()
    
    if overlap_left < overlap_right and overlap_bottom < overlap_top:
        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_top - overlap_bottom
        overlap_area = overlap_width * overlap_height
        print(f"Overlap area = {overlap_width} × {overlap_height} = {overlap_area}")
    else:
        overlap_area = 0
        print("No overlap (boundaries don't form valid rectangle)")
    
    total_area = area_a + area_b - overlap_area
    print(f"\nTotal area = {area_a} + {area_b} - {overlap_area} = {total_area}")
    
    # Visual representation concept
    print("\nKey insight: Total Area = Area A + Area B - Overlap Area")
    print("This prevents double-counting the overlapped region.")