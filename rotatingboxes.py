# LeetCode 1861: Rotating the Box

class Solution:
    # Approach 1: Two-step process (Rotate then Apply Gravity)
    def rotateTheBox(self, boxGrid):
        m, n = len(boxGrid), len(boxGrid[0])
        
        # Step 1: Apply gravity to each row (stones fall to the right)
        for row in boxGrid:
            self.apply_gravity_to_row(row)
        
        # Step 2: Rotate 90 degrees clockwise
        # After rotation: result[j][m-1-i] = original[i][j]
        result = [['.' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = boxGrid[i][j]
        
        return result
    
    def apply_gravity_to_row(self, row):
        """Apply gravity to make stones fall to the right in a single row"""
        n = len(row)
        # Use two pointers: write_pos for where to place next stone
        write_pos = n - 1
        
        # Process from right to left
        for read_pos in range(n - 1, -1, -1):
            if row[read_pos] == '*':
                # Obstacle: reset write position
                write_pos = read_pos - 1
            elif row[read_pos] == '#':
                # Stone: move it to write_pos
                if write_pos != read_pos:
                    row[write_pos] = '#'
                    row[read_pos] = '.'
                write_pos -= 1
            # Empty space: do nothing, just continue
        
    # Approach 2: Direct construction (more efficient)
    def rotateTheBox_direct(self, boxGrid):
        m, n = len(boxGrid), len(boxGrid[0])
        result = [['.' for _ in range(m)] for _ in range(n)]
        
        # Process each original row
        for i in range(m):
            # Apply gravity to current row and place in rotated position
            stones, obstacles = self.count_stones_and_obstacles(boxGrid[i])
            self.fill_rotated_column(result, stones, obstacles, m - 1 - i)
        
        return result
    
    def count_stones_and_obstacles(self, row):
        """Count stones and record obstacle positions in a row"""
        stones = []
        obstacles = []
        stone_count = 0
        
        for j, cell in enumerate(row):
            if cell == '#':
                stone_count += 1
            elif cell == '*':
                obstacles.append(j)
                stones.append(stone_count)
                stone_count = 0
        
        # Don't forget stones after the last obstacle
        stones.append(stone_count)
        return stones, obstacles
    
    def fill_rotated_column(self, result, stones, obstacles, col):
        """Fill a column in the rotated matrix with stones and obstacles"""
        n = len(result)
        stone_idx = 0
        current_stone_count = stones[0] if stones else 0
        
        # Fill from bottom to top (gravity effect)
        bottom = n - 1
        
        # Place obstacles first
        for obs_pos in obstacles:
            result[obs_pos][col] = '*'
        
        # Fill segments between obstacles
        segment_start = 0
        for obs_pos in obstacles:
            # Fill segment from segment_start to obs_pos-1
            stone_count = stones[stone_idx]
            # Place stones at the bottom of this segment
            for pos in range(obs_pos - 1, obs_pos - 1 - stone_count, -1):
                result[pos][col] = '#'
            segment_start = obs_pos + 1
            stone_idx += 1
        
        # Fill last segment (from last obstacle to end)
        if stone_idx < len(stones):
            stone_count = stones[stone_idx]
            for pos in range(n - 1, n - 1 - stone_count, -1):
                result[pos][col] = '#'
    
    # Approach 3: Step-by-step simulation (most readable)
    def rotateTheBox_simulation(self, boxGrid):
        m, n = len(boxGrid), len(boxGrid[0])
        
        # Step 1: Create a copy and apply gravity
        box_after_gravity = [row[:] for row in boxGrid]  # Deep copy
        
        for i in range(m):
            # Apply gravity to each row independently
            row = box_after_gravity[i]
            # Simulate stones falling to the right
            for _ in range(n):  # At most n iterations needed
                moved = False
                for j in range(n - 2, -1, -1):  # Right to left
                    if row[j] == '#' and row[j + 1] == '.':
                        # Stone can fall to the right
                        row[j], row[j + 1] = '.', '#'
                        moved = True
                if not moved:
                    break  # No more stones can fall
        
        # Step 2: Rotate 90 degrees clockwise
        result = [['.' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = box_after_gravity[i][j]
        
        return result

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # Example 1
        [["#", ".", "#"]],
        
        # Example 2  
        [["#", ".", "*", "."],
         ["#", "#", "*", "."]],
        
        # Example 3
        [["#", "#", "*", ".", "*", "."],
         ["#", "#", "#", "*", ".", "."],
         ["#", "#", "#", ".", "#", "."]],
        
        # Edge cases
        [["*"]],  # Only obstacle
        [["."]], # Only empty
        [["#"]], # Only stone
        [["#", "*", "#", ".", "#"]]  # Mixed single row
    ]
    
    expected_outputs = [
        # Example 1
        [[".",],
         ["#"],
         ["#"]],
        
        # Example 2
        [["#", "."],
         ["#", "#"], 
         ["*", "*"],
         [".", "."]],
        
        # Example 3
        [[".", "#", "#"],
         [".", "#", "#"],
         ["#", "#", "*"],
         ["#", "*", "."],
         ["#", ".", "*"],
         ["#", ".", "."]],
        
        # Edge cases
        [["*"]], 
        [["."]],
        [["#"]],
        [["#"], ["*"], ["#"], ["."], ["#"]]
    ]
    
    approaches = [
        ("Two-step (Optimal)", solution.rotateTheBox),
        ("Simulation", solution.rotateTheBox_simulation)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        for i, (box_grid, expected) in enumerate(zip(test_cases, expected_outputs)):
            result = method(box_grid)
            # Simple comparison for testing
            matches = len(result) == len(expected) and all(
                len(result[r]) == len(expected[r]) and 
                all(result[r][c] == expected[r][c] for c in range(len(result[r])))
                for r in range(len(result))
            )
            status = "✓" if matches else "✗"
            print(f"  {status} Test case {i+1}")
            if not matches:
                print(f"    Expected: {expected}")
                print(f"    Got:      {result}")
        print()
    
    # Demonstrate step-by-step for Example 2
    print("Step-by-step demonstration for Example 2:")
    box_grid = [["#", ".", "*", "."],
                ["#", "#", "*", "."]]
    
    print("Original:")
    for row in box_grid:
        print("  " + " ".join(row))
    
    # Apply gravity
    for row in box_grid:
        solution.apply_gravity_to_row(row)
    
    print("\nAfter gravity (stones fall right):")
    for row in box_grid:
        print("  " + " ".join(row))
    
    # Rotate
    m, n = len(box_grid), len(box_grid[0])
    result = [['.' for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][m - 1 - i] = box_grid[i][j]
    
    print("\nAfter 90° clockwise rotation:")
    for row in result:
        print("  " + " ".join(row))