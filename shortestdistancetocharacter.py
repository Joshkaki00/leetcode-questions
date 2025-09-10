# LeetCode 821: Shortest Distance to a Character

class Solution:
    # Approach 1: Two-pass algorithm (Optimal)
    def shortestToChar(self, s, c):
        n = len(s)
        answer = [float('inf')] * n
        
        # First pass: left to right
        # Track distance from previous occurrence of c
        prev_c_pos = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev_c_pos = i
            answer[i] = i - prev_c_pos
        
        # Second pass: right to left  
        # Update with distance from next occurrence of c
        next_c_pos = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                next_c_pos = i
            answer[i] = min(answer[i], next_c_pos - i)
        
        return answer
    
    # Approach 2: Find all positions first
    def shortestToChar_positions(self, s, c):
        n = len(s)
        
        # Find all positions of character c
        c_positions = []
        for i in range(n):
            if s[i] == c:
                c_positions.append(i)
        
        answer = []
        
        # For each position, find distance to closest c
        for i in range(n):
            min_distance = float('inf')
            for pos in c_positions:
                distance = abs(i - pos)
                min_distance = min(min_distance, distance)
            answer.append(min_distance)
        
        return answer
    
    # Approach 3: Binary search optimization
    def shortestToChar_binary_search(self, s, c):
        import bisect
        
        n = len(s)
        
        # Find all positions of character c
        c_positions = [i for i in range(n) if s[i] == c]
        
        answer = []
        
        # For each position, use binary search to find closest c
        for i in range(n):
            # Find insertion point
            pos = bisect.bisect_left(c_positions, i)
            
            min_distance = float('inf')
            
            # Check position to the left
            if pos > 0:
                min_distance = min(min_distance, i - c_positions[pos - 1])
            
            # Check position to the right
            if pos < len(c_positions):
                min_distance = min(min_distance, c_positions[pos] - i)
            
            answer.append(min_distance)
        
        return answer
    
    # Approach 4: Brute force (for understanding)
    def shortestToChar_brute(self, s, c):
        n = len(s)
        answer = []
        
        for i in range(n):
            min_distance = float('inf')
            
            # Check distance to every occurrence of c
            for j in range(n):
                if s[j] == c:
                    distance = abs(i - j)
                    min_distance = min(min_distance, distance)
            
            answer.append(min_distance)
        
        return answer
    
    # Approach 5: Dynamic programming style
    def shortestToChar_dp(self, s, c):
        n = len(s)
        
        # dp[i] = shortest distance from position i to character c
        dp = [float('inf')] * n
        
        # Initialize positions where c occurs
        for i in range(n):
            if s[i] == c:
                dp[i] = 0
        
        # Forward pass: propagate distances from left
        for i in range(1, n):
            dp[i] = min(dp[i], dp[i-1] + 1)
        
        # Backward pass: propagate distances from right
        for i in range(n - 2, -1, -1):
            dp[i] = min(dp[i], dp[i+1] + 1)
        
        return dp

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("loveleetcode", "e", [3,2,1,0,1,0,0,1,2,2,1,0]),  # Example 1
        ("aaab", "b", [3,2,1,0]),                           # Example 2
        ("abaa", "a", [0,1,0,0]),                           # Multiple a's
        ("c", "c", [0]),                                    # Single character
        ("abcde", "c", [2,1,0,1,2]),                        # Middle character
        ("aaa", "a", [0,0,0]),                              # All same character
        ("abcabc", "a", [0,1,2,0,1,2]),                     # Repeated pattern
        ("hello", "l", [2,1,0,0,1])                         # Adjacent characters
    ]
    
    approaches = [
        ("Two-pass (Optimal)", solution.shortestToChar),
        ("Find Positions", solution.shortestToChar_positions),
        ("Binary Search", solution.shortestToChar_binary_search),
        ("Brute Force", solution.shortestToChar_brute),
        ("Dynamic Programming", solution.shortestToChar_dp)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for s, c, expected in test_cases:
            result = method(s, c)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} s='{s}', c='{c}' → {result} (expected: {expected})")
            else:
                print(f"  {status} s='{s}', c='{c}' → {result}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed trace for Example 1: "loveleetcode", "e"
    print("Detailed trace for 'loveleetcode', 'e':")
    s = "loveleetcode"
    c = "e"
    n = len(s)
    
    print(f"String: {s}")
    print(f"Target: '{c}'")
    print(f"Positions of '{c}': {[i for i in range(n) if s[i] == c]}")
    print()
    
    # Trace two-pass algorithm
    answer = [float('inf')] * n
    
    print("First pass (left to right):")
    prev_c_pos = float('-inf')
    for i in range(n):
        if s[i] == c:
            prev_c_pos = i
        answer[i] = i - prev_c_pos
        print(f"  i={i}, char='{s[i]}', prev_c_pos={prev_c_pos}, distance={answer[i]}")
    
    print(f"After first pass: {answer}")
    print()
    
    print("Second pass (right to left):")
    next_c_pos = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            next_c_pos = i
        old_distance = answer[i]
        answer[i] = min(answer[i], next_c_pos - i)
        print(f"  i={i}, char='{s[i]}', next_c_pos={next_c_pos}, old={old_distance}, new={answer[i]}")
    
    print(f"Final result: {answer}")
    
    # Verify each position manually
    print("\nManual verification:")
    c_positions = [i for i in range(n) if s[i] == c]
    for i in range(n):
        distances = [abs(i - pos) for pos in c_positions]
        min_dist = min(distances)
        print(f"  Position {i} ('{s[i]}'): distances to 'e' = {distances}, min = {min_dist}")
    
    print("\nAlgorithm insights:")
    print("- Two-pass approach ensures we consider both left and right directions")
    print("- First pass: distance from nearest 'e' on the left")
    print("- Second pass: update with distance from nearest 'e' on the right")
    print("- Final answer is minimum of both directions")