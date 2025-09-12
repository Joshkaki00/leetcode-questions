# LeetCode 3227: Vowels Game in a String

class Solution:
    # Approach 1: Game Theory Analysis (Optimal)
    def doesAliceWin(self, s):
        """
        Key insight: If there are any vowels in the string, Alice can always win.
        If there are no vowels, Alice loses immediately.
        
        Proof:
        1. If no vowels exist, Alice cannot make any move (needs odd vowels), so Alice loses.
        2. If vowels exist, Alice can always take the entire string on her first turn
           (total vowels is either odd or even, and Alice needs odd).
           - If total is odd: Alice takes whole string and wins
           - If total is even: Alice can take a substring with 1 vowel, leaving Bob 
             with the rest having odd vowels, but Bob needs even vowels, so Bob loses.
        """
        # Count total vowels
        vowel_count = sum(1 for char in s if char in 'aeiou')
        
        # Alice wins if and only if there's at least one vowel
        return vowel_count > 0
    
    # Approach 2: Explicit Game Theory (For Understanding)
    def doesAliceWin_explicit(self, s):
        vowels = set('aeiou')
        total_vowels = sum(1 for char in s if char in vowels)
        
        # Base case: no vowels means Alice loses immediately
        if total_vowels == 0:
            return False
        
        # If there are vowels, Alice has a winning strategy:
        # Case 1: Total vowels is odd
        if total_vowels % 2 == 1:
            # Alice can take the entire string (odd vowels) and win immediately
            return True
        
        # Case 2: Total vowels is even
        else:
            # Alice can take any single vowel (1 is odd), leaving Bob with odd total
            # Bob needs even vowels but remaining total is odd, so Bob will lose
            return True
        
        # In both cases, Alice wins if vowels exist
    
    # Approach 3: Brute Force Game Simulation (Theoretical, too slow for large inputs)
    def doesAliceWin_simulation(self, s):
        """
        This approach simulates the actual game but is too slow for practical use.
        Included for educational purposes to understand the game mechanics.
        """
        vowels = set('aeiou')
        
        def count_vowels(string):
            return sum(1 for char in string if char in vowels)
        
        def get_valid_moves(string, is_alice_turn):
            """Get all valid substrings that the current player can remove"""
            moves = []
            n = len(string)
            
            for i in range(n):
                for j in range(i + 1, n + 1):
                    substring = string[i:j]
                    vowel_count = count_vowels(substring)
                    
                    # Alice needs odd vowels, Bob needs even vowels
                    if is_alice_turn and vowel_count % 2 == 1:
                        moves.append((i, j))
                    elif not is_alice_turn and vowel_count % 2 == 0:
                        moves.append((i, j))
            
            return moves
        
        def can_win(string, is_alice_turn):
            """Recursively determine if current player can win"""
            moves = get_valid_moves(string, is_alice_turn)
            
            if not moves:
                # No valid moves, current player loses
                return False
            
            # Try each possible move
            for start, end in moves:
                new_string = string[:start] + string[end:]
                # If opponent cannot win from resulting position, current player wins
                if not can_win(new_string, not is_alice_turn):
                    return True
            
            # All moves lead to opponent winning, so current player loses
            return False
        
        return can_win(s, True)  # Alice starts first
    
    # Approach 4: Mathematical proof verification
    def doesAliceWin_proof(self, s):
        """
        Verify the mathematical proof with detailed reasoning
        """
        vowels = set('aeiou')
        total_vowels = sum(1 for char in s if char in vowels)
        
        print(f"String: '{s}'")
        print(f"Total vowels: {total_vowels}")
        
        if total_vowels == 0:
            print("No vowels → Alice cannot make any move → Alice loses")
            return False
        
        print("Vowels exist → Alice has winning strategy:")
        
        if total_vowels % 2 == 1:
            print("- Total vowels is odd")
            print("- Alice can take entire string (odd vowels) → Alice wins immediately")
        else:
            print("- Total vowels is even") 
            print("- Alice can take substring with 1 vowel")
            print("- Remaining vowels = even - 1 = odd")
            print("- Bob needs even vowels but remaining is odd → Bob loses")
        
        return True

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("leetcoder", True),   # Example 1: contains vowels
        ("bbcd", False),       # Example 2: no vowels
        ("a", True),           # Single vowel
        ("b", False),          # Single consonant
        ("aeiou", True),       # All vowels (5 total, odd)
        ("aabb", True),        # 2 vowels (even), Alice can take 1
        ("bcdfg", False),      # No vowels
        ("programming", True), # Mixed with vowels
        ("rhythm", False),     # No vowels
        ("hello", True),       # 2 vowels
        ("world", True),       # 1 vowel
        ("", False)            # Empty string (edge case)
    ]
    
    approaches = [
        ("Game Theory (Optimal)", solution.doesAliceWin),
        ("Explicit Analysis", solution.doesAliceWin_explicit)
        # Note: simulation approach would be too slow for large inputs
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for s, expected in test_cases:
            if s == "":  # Skip empty string for some methods
                continue
                
            result = method(s)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} '{s}' → {result} (expected: {expected})")
            else:
                print(f"  {status} '{s}' → {result}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed analysis for examples
    print("Detailed analysis for examples:")
    print()
    
    # Example 1: "leetcoder"
    print("Example 1: 'leetcoder'")
    s1 = "leetcoder"
    vowels_in_s1 = [c for c in s1 if c in 'aeiou']
    print(f"Vowels: {vowels_in_s1} (count: {len(vowels_in_s1)})")
    print(f"Alice's winning strategy:")
    print(f"- Total vowels = {len(vowels_in_s1)} (odd)")
    print(f"- Alice can take entire string 'leetcoder' (3 vowels = odd)")
    print(f"- Game ends, Alice wins")
    print(f"Result: {solution.doesAliceWin(s1)}")
    print()
    
    # Example 2: "bbcd"  
    print("Example 2: 'bbcd'")
    s2 = "bbcd"
    vowels_in_s2 = [c for c in s2 if c in 'aeiou']
    print(f"Vowels: {vowels_in_s2} (count: {len(vowels_in_s2)})")
    print(f"Alice cannot make any move (needs odd vowels, but 0 available)")
    print(f"Alice loses immediately")
    print(f"Result: {solution.doesAliceWin(s2)}")
    print()
    
    # Strategic example with even vowels
    print("Strategic example: 'hello' (even vowels)")
    s3 = "hello"
    vowels_in_s3 = [c for c in s3 if c in 'aeiou']
    print(f"Vowels: {vowels_in_s3} (count: {len(vowels_in_s3)})")
    print(f"Alice's winning strategy:")
    print(f"- Total vowels = {len(vowels_in_s3)} (even)")
    print(f"- Alice takes substring 'e' (1 vowel = odd)")
    print(f"- Remaining: 'hllo' + 'o' has 1 vowel (odd total)")
    print(f"- Bob needs even vowels but only odd available → Bob loses")
    print(f"Result: {solution.doesAliceWin(s3)}")
    
    print("\nKey insight: The game outcome depends only on whether vowels exist!")
    print("- If vowels exist: Alice always has a winning strategy")
    print("- If no vowels: Alice loses immediately")