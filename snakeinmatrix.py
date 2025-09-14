# LeetCode 3248: Snake in Matrix

class Solution:
    # Approach 1: Track position directly using formula (Optimal)
    def finalPositionOfSnake(self, n, commands):
        """
        Track snake position using the given formula: grid[i][j] = (i * n) + j
        Start at position 0, update position based on commands.
        """
        position = 0  # Starting position
        
        for command in commands:
            # Calculate current row and column from position
            row = position // n
            col = position % n
            
            # Update row and column based on command
            if command == "UP":
                row -= 1
            elif command == "DOWN":
                row += 1
            elif command == "LEFT":
                col -= 1
            elif command == "RIGHT":
                col += 1
            
            # Convert back to position using the formula
            position = row * n + col
        
        return position
    
    # Approach 2: Simulate with row/col tracking (Alternative)
    def finalPositionOfSnake_rowcol(self, n, commands):
        """
        Track row and column separately, convert to position at the end.
        """
        row, col = 0, 0  # Starting at grid[0][0]
        
        for command in commands:
            if command == "UP":
                row -= 1
            elif command == "DOWN":
                row += 1
            elif command == "LEFT":
                col -= 1
            elif command == "RIGHT":
                col += 1
        
        # Convert final row,col to position
        return row * n + col
    
    # Approach 3: Using direction vectors (More scalable)
    def finalPositionOfSnake_vectors(self, n, commands):
        """
        Use direction vectors for movement calculations.
        """
        # Direction vectors: UP, DOWN, LEFT, RIGHT
        directions = {
            "UP": (-1, 0),
            "DOWN": (1, 0), 
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        
        row, col = 0, 0
        
        for command in commands:
            dr, dc = directions[command]
            row += dr
            col += dc
        
        return row * n + col
    
    # Approach 4: Mathematical optimization (Most efficient)
    def finalPositionOfSnake_math(self, n, commands):
        """
        Optimize by tracking net movement without intermediate conversions.
        """
        net_row_moves = 0
        net_col_moves = 0
        
        for command in commands:
            if command == "UP":
                net_row_moves -= 1
            elif command == "DOWN":
                net_row_moves += 1
            elif command == "LEFT":
                net_col_moves -= 1
            elif command == "RIGHT":
                net_col_moves += 1
        
        # Final position calculation
        final_row = 0 + net_row_moves
        final_col = 0 + net_col_moves
        
        return final_row * n + final_col

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # Example 1: n=2, commands=["RIGHT","DOWN"]
        (2, ["RIGHT", "DOWN"], 3),
        
        # Example 2: n=3, commands=["DOWN","RIGHT","UP"] 
        (3, ["DOWN", "RIGHT", "UP"], 1),
        
        # Additional test cases
        (2, ["RIGHT"], 1),           # Simple right move
        (2, ["DOWN"], 2),            # Simple down move
        (3, [], 0),                  # No commands, stay at start
        (3, ["RIGHT", "RIGHT"], 2),  # Multiple right moves
        (3, ["DOWN", "DOWN"], 6),    # Multiple down moves
        (4, ["RIGHT", "DOWN", "LEFT", "UP"], 0),  # Return to start
        (3, ["DOWN", "RIGHT", "DOWN", "LEFT"], 6)  # Complex path
    ]
    
    approaches = [
        ("Direct Position Tracking", solution.finalPositionOfSnake),
        ("Row/Col Tracking", solution.finalPositionOfSnake_rowcol),
        ("Direction Vectors", solution.finalPositionOfSnake_vectors),
        ("Mathematical Optimization", solution.finalPositionOfSnake_math)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for n, commands, expected in test_cases:
            result = method(n, commands)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} n={n}, commands={commands} → {result} (expected: {expected})")
            else:
                print(f"  {status} n={n}, commands={commands} → {result}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed trace for Example 1: n=2, commands=["RIGHT","DOWN"]
    print("Detailed trace for Example 1: n=2, commands=['RIGHT','DOWN']")
    n = 2
    commands = ["RIGHT", "DOWN"]
    
    print(f"Grid size: {n}x{n}")
    print("Grid positions:")
    for i in range(n):
        row_positions = []
        for j in range(n):
            pos = i * n + j
            row_positions.append(f"{pos}")
        print(f"  Row {i}: {' '.join(row_positions)}")
    
    print(f"\nStarting position: 0 (row=0, col=0)")
    
    position = 0
    row, col = 0, 0
    
    for i, command in enumerate(commands):
        print(f"\nStep {i+1}: Command '{command}'")
        print(f"  Before: position={position}, row={row}, col={col}")
        
        if command == "UP":
            row -= 1
        elif command == "DOWN":
            row += 1
        elif command == "LEFT":
            col -= 1
        elif command == "RIGHT":
            col += 1
        
        position = row * n + col
        print(f"  After:  position={position}, row={row}, col={col}")
    
    print(f"\nFinal position: {position}")
    
    # Detailed trace for Example 2: n=3, commands=["DOWN","RIGHT","UP"]
    print("\nDetailed trace for Example 2: n=3, commands=['DOWN','RIGHT','UP']")
    n = 3
    commands = ["DOWN", "RIGHT", "UP"]
    
    print(f"Grid size: {n}x{n}")
    print("Grid positions:")
    for i in range(n):
        row_positions = []
        for j in range(n):
            pos = i * n + j
            row_positions.append(f"{pos}")
        print(f"  Row {i}: {' '.join(row_positions)}")
    
    position = 0
    row, col = 0, 0
    print(f"\nStarting position: 0 (row=0, col=0)")
    
    for i, command in enumerate(commands):
        print(f"\nStep {i+1}: Command '{command}'")
        print(f"  Before: position={position}, row={row}, col={col}")
        
        if command == "UP":
            row -= 1
        elif command == "DOWN":
            row += 1
        elif command == "LEFT":
            col -= 1
        elif command == "RIGHT":
            col += 1
        
        position = row * n + col
        print(f"  After:  position={position}, row={row}, col={col}")
    
    print(f"\nFinal position: {position}")
    
    print("\nKey insights:")
    print("- Position formula: grid[i][j] = (i * n) + j")
    print("- Convert position to row/col: row = pos // n, col = pos % n")
    print("- Convert row/col to position: position = row * n + col")
    print("- All approaches have O(C) time complexity where C = number of commands")