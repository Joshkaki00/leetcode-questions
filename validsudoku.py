# LeetCode 36: Valid Sudoku

class Solution:
    # Approach 1: Three separate passes (most readable)
    def isValidSudoku_three_passes(self, board):
        # Check all rows
        for row in board:
            if not self.is_valid_unit(row):
                return False
        
        # Check all columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid_unit(column):
                return False
        
        # Check all 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[box_row * 3 + i][box_col * 3 + j])
                if not self.is_valid_unit(box):
                    return False
        
        return True
    
    def is_valid_unit(self, unit):
        """Check if a unit (row, column, or box) is valid"""
        seen = set()
        for cell in unit:
            if cell != '.' and cell in seen:
                return False
            if cell != '.':
                seen.add(cell)
        return True
    
    # Approach 2: Single pass with sets (Optimal)
    def isValidSudoku(self, board):
        # Use sets to track seen numbers in rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                
                # Skip empty cells
                if cell == '.':
                    continue
                
                # Calculate which 3x3 box this cell belongs to
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check if number already exists in row, column, or box
                if (cell in rows[i] or 
                    cell in cols[j] or 
                    cell in boxes[box_index]):
                    return False
                
                # Add number to corresponding sets
                rows[i].add(cell)
                cols[j].add(cell)
                boxes[box_index].add(cell)
        
        return True
    
    # Approach 3: Using strings to track seen values (space optimized)
    def isValidSudoku_string_sets(self, board):
        seen = set()
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell != '.':
                    # Create unique identifiers for each constraint
                    row_key = f"row{i}-{cell}"
                    col_key = f"col{j}-{cell}"
                    box_key = f"box{i//3}{j//3}-{cell}"
                    
                    # Check if any constraint is violated
                    if row_key in seen or col_key in seen or box_key in seen:
                        return False
                    
                    # Add all constraints to seen set
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)
        
        return True
    
    # Approach 4: Bit manipulation (advanced)
    def isValidSudoku_bits(self, board):
        # Use bitmasks to track seen digits (1-9 map to bits 0-8)
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue
                
                # Convert digit to bit position (1->0, 2->1, ..., 9->8)
                bit = 1 << (int(cell) - 1)
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check if bit is already set (number already seen)
                if (rows[i] & bit) or (cols[j] & bit) or (boxes[box_index] & bit):
                    return False
                
                # Set the bit (mark number as seen)
                rows[i] |= bit
                cols[j] |= bit
                boxes[box_index] |= bit
        
        return True

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    # Valid Sudoku board (Example 1)
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    # Invalid Sudoku board (Example 2 - two 8's in top-left box)
    invalid_board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    test_cases = [
        (valid_board, True, "Valid board"),
        (invalid_board, False, "Invalid board (duplicate 8 in top-left box)")
    ]
    
    approaches = [
        ("Single Pass (Optimal)", solution.isValidSudoku),
        ("Three Passes", solution.isValidSudoku_three_passes),
        ("String Sets", solution.isValidSudoku_string_sets),
        ("Bit Manipulation", solution.isValidSudoku_bits)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        for board, expected, description in test_cases:
            result = method(board)
            status = "✓" if result == expected else "✗"
            print(f"  {status} {description}: {result}")
        print()
    
    # Test edge cases
    print("Edge case tests:")
    
    # All empty board
    empty_board = [["." for _ in range(9)] for _ in range(9)]
    result = solution.isValidSudoku(empty_board)
    print(f"All empty board: {result} (should be True)")
    
    # Row with duplicate
    row_duplicate = [
        ["1","2","3","4","5","6","7","8","1"],  # Two 1's in row
        ["." for _ in range(9)] for _ in range(8)
    ]
    result = solution.isValidSudoku(row_duplicate)
    print(f"Row duplicate: {result} (should be False)")
    
    # Column with duplicate  
    col_duplicate = [["." for _ in range(9)] for _ in range(9)]
    col_duplicate[0][0] = "5"
    col_duplicate[5][0] = "5"  # Same column, duplicate 5
    result = solution.isValidSudoku(col_duplicate)
    print(f"Column duplicate: {result} (should be False)")