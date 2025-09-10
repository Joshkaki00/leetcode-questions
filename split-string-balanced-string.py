# LeetCode 1221: Split a String in Balanced Strings

class Solution:
    # Approach 1: Greedy with Balance Counter (Optimal)
    def balancedStringSplit(self, s):
        balance = 0  # Track balance: +1 for 'R', -1 for 'L'
        count = 0    # Count of balanced substrings
        
        for char in s:
            # Update balance
            if char == 'R':
                balance += 1
            else:  # char == 'L'
                balance -= 1
            
            # When balance reaches 0, we have a balanced substring
            if balance == 0:
                count += 1
        
        return count
    
    # Approach 2: Explicit Counting (Alternative)
    def balancedStringSplit_explicit(self, s):
        r_count = 0
        l_count = 0
        balanced_count = 0
        
        for char in s:
            if char == 'R':
                r_count += 1
            else:  # char == 'L'
                l_count += 1
            
            # Check if current substring is balanced
            if r_count == l_count:
                balanced_count += 1
                # Reset counters for next substring
                r_count = 0
                l_count = 0
        
        return balanced_count
    
    # Approach 3: Stack-based (for understanding)
    def balancedStringSplit_stack(self, s):
        stack = []
        balanced_count = 0
        
        for char in s:
            if not stack or stack[-1] == char:
                # Empty stack or same character - push
                stack.append(char)
            else:
                # Different character - they balance out
                stack.pop()
                
                # If stack becomes empty, we have a balanced substring
                if not stack:
                    balanced_count += 1
        
        return balanced_count
    
    # Approach 4: Recursive (for completeness)
    def balancedStringSplit_recursive(self, s):
        def find_balanced_substrings(index, current_balance):
            if index == len(s):
                return 0
            
            # Update balance for current character
            if s[index] == 'R':
                current_balance += 1
            else:
                current_balance -= 1
            
            # If balanced, we can split here and start fresh
            if current_balance == 0:
                return 1 + find_balanced_substrings(index + 1, 0)
            else:
                return find_balanced_substrings(index + 1, current_balance)
        
        return find_balanced_substrings(0, 0)
    
    # Approach 5: With detailed tracking (for debugging)
    def balancedStringSplit_debug(self, s):
        balance = 0
        count = 0
        splits = []  # Track where splits occur
        start = 0
        
        for i, char in enumerate(s):
            if char == 'R':
                balance += 1
            else:
                balance -= 1
            
            if balance == 0:
                # Found a balanced substring
                substring = s[start:i+1]
                splits.append(substring)
                count += 1
                start = i + 1
        
        # For debugging purposes (not needed for LeetCode)
        # print(f"Splits: {splits}")
        return count

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("RLRRLLRLRL", 4),    # Example 1: "RL", "RRLL", "RL", "RL"
        ("RLRRRLLRLL", 2),    # Example 2: "RL", "RRRLLRLL"  
        ("LLLLRRRR", 1),      # Example 3: "LLLLRRRR"
        ("RL", 1),            # Simple case
        ("RLRL", 2),          # "RL", "RL"
        ("RRLLRRLL", 2),      # "RRLL", "RRLL"
        ("LRLRLRLR", 4),      # "LR", "LR", "LR", "LR" (but actually "L" first)
        ("RLLR", 1),          # "RLLR"
        ("RRLLLLRR", 1),      # "RRLLLLRR"
        ("LRLRLR", 3)         # "LR", "LR", "LR"
    ]
    
    approaches = [
        ("Greedy (Optimal)", solution.balancedStringSplit),
        ("Explicit Counting", solution.balancedStringSplit_explicit),
        ("Stack-based", solution.balancedStringSplit_stack),
        ("Recursive", solution.balancedStringSplit_recursive),
        ("Debug Version", solution.balancedStringSplit_debug)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for s, expected in test_cases:
            result = method(s)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} '{s}' → {result} (expected: {expected})")
            else:
                print(f"  {status} '{s}' → {result}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed trace for Example 1: "RLRRLLRLRL"
    print("Detailed trace for 'RLRRLLRLRL':")
    s = "RLRRLLRLRL"
    balance = 0
    count = 0
    
    print(f"String: {s}")
    print("Step-by-step balance tracking:")
    
    for i, char in enumerate(s):
        if char == 'R':
            balance += 1
        else:
            balance -= 1
        
        print(f"  i={i}, char='{char}', balance={balance}", end="")
        
        if balance == 0:
            count += 1
            print(f" → Split #{count} found! Substring: '{s[:i+1] if count == 1 else 'next segment'}'")
        else:
            print()
    
    print(f"Total balanced substrings: {count}")
    
    # Show the actual splits for Example 1
    print("\nActual splits for 'RLRRLLRLRL':")
    balance = 0
    start = 0
    splits = []
    
    for i, char in enumerate(s):
        if char == 'R':
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            substring = s[start:i+1]
            splits.append(substring)
            start = i + 1
    
    print(f"Splits: {splits}")
    print(f"Lengths: {[len(split) for split in splits]}")
    
    # Verify each split is balanced
    print("\nVerification - each split is balanced:")
    for i, split in enumerate(splits):
        r_count = split.count('R')
        l_count = split.count('L')
        print(f"  Split {i+1}: '{split}' → R={r_count}, L={l_count}, Balanced={r_count==l_count}")
    
    print("\nKey insight: Greedy approach works because:")
    print("- We want to maximize the number of splits")
    print("- Splitting early never prevents future splits")
    print("- If we can split at position i, there's no benefit to waiting")
    print("- The remaining string is still guaranteed to be balanced")