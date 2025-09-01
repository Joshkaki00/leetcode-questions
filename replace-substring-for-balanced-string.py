# LeetCode 1234: Replace the Substring for Balanced String

class Solution:
    # Approach 1: Sliding Window (Optimal)
    def balancedString(self, s):
        n = len(s)
        target = n // 4  # Each character should appear exactly this many times
        
        # Count current frequency of each character
        count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for char in s:
            count[char] += 1
        
        # Calculate excess characters (characters that appear more than target)
        excess = {}
        for char in 'QWER':
            if count[char] > target:
                excess[char] = count[char] - target
        
        # If no excess, string is already balanced
        if not excess:
            return 0
        
        # Use sliding window to find minimum substring containing all excess
        left = 0
        min_length = n
        window_count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        
        for right in range(n):
            # Expand window by including s[right]
            window_count[s[right]] += 1
            
            # Contract window from left while it's valid
            while self.is_valid_window(window_count, excess):
                min_length = min(min_length, right - left + 1)
                window_count[s[left]] -= 1
                left += 1
        
        return min_length
    
    def is_valid_window(self, window_count, excess):
        """Check if current window contains enough excess characters"""
        for char, needed in excess.items():
            if window_count[char] < needed:
                return False
        return True
    
    # Approach 2: Sliding Window with Counter (Alternative)
    def balancedString_counter(self, s):
        from collections import Counter
        
        n = len(s)
        target = n // 4
        count = Counter(s)
        
        # Find characters that exceed the target
        excess = {}
        for char in 'QWER':
            if count[char] > target:
                excess[char] = count[char] - target
        
        if not excess:
            return 0
        
        # Sliding window to find minimum substring
        left = 0
        min_length = n
        
        for right in range(n):
            # Include current character in window by reducing its count
            if s[right] in excess:
                excess[s[right]] -= 1
            
            # Contract window while all excess characters are covered
            while all(count <= 0 for count in excess.values()):
                min_length = min(min_length, right - left + 1)
                
                # Remove left character from window
                if s[left] in excess:
                    excess[s[left]] += 1
                left += 1
        
        return min_length
    
    # Approach 3: Brute Force (for understanding)
    def balancedString_brute(self, s):
        n = len(s)
        target = n // 4
        
        def count_chars(string):
            count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
            for char in string:
                count[char] += 1
            return count
        
        def is_balanced_after_replacement(original_count, substring_count):
            """Check if string becomes balanced after replacing substring"""
            for char in 'QWER':
                remaining = original_count[char] - substring_count[char]
                # After replacement, we can have at most 'target' of each char
                if remaining > target:
                    return False
            return True
        
        original_count = count_chars(s)
        
        # Check if already balanced
        if all(original_count[char] == target for char in 'QWER'):
            return 0
        
        # Try all possible substrings
        for length in range(1, n + 1):
            for start in range(n - length + 1):
                substring = s[start:start + length]
                substring_count = count_chars(substring)
                
                if is_balanced_after_replacement(original_count, substring_count):
                    return length
        
        return n  # Worst case: replace entire string
    
    # Approach 4: Optimized Sliding Window with Early Termination
    def balancedString_optimized(self, s):
        n = len(s)
        target = n // 4
        
        # Count frequencies
        freq = [0] * 128  # ASCII array for faster access
        for char in s:
            freq[ord(char)] += 1
        
        # Calculate excess for each character
        excess_Q = max(0, freq[ord('Q')] - target)
        excess_W = max(0, freq[ord('W')] - target)  
        excess_E = max(0, freq[ord('E')] - target)
        excess_R = max(0, freq[ord('R')] - target)
        
        # If no excess, already balanced
        if excess_Q + excess_W + excess_E + excess_R == 0:
            return 0
        
        left = 0
        min_length = n
        window = [0] * 128
        
        for right in range(n):
            window[ord(s[right])] += 1
            
            # Contract window while valid
            while (window[ord('Q')] >= excess_Q and
                   window[ord('W')] >= excess_W and
                   window[ord('E')] >= excess_E and
                   window[ord('R')] >= excess_R):
                
                min_length = min(min_length, right - left + 1)
                window[ord(s[left])] -= 1
                left += 1
        
        return min_length

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("QWER", 0),        # Already balanced
        ("QQWE", 1),        # Need to replace 1 'Q' 
        ("QQQW", 2),        # Need to replace 2 'Q's
        ("QQQQQWWWRRRR", 4), # More complex case
        ("QQQQWWWWEEERRR", 3), # Another complex case
        ("QWERQWERQWERQWER", 0), # Already balanced, longer
        ("QQQQWWWWEEERRRRR", 1), # One excess R
        ("QQQWWWEEERR", 2),     # Need to balance multiple chars
        ("WWEQERQWQWWRWWERQWEQ", 4) # Complex case
    ]
    
    approaches = [
        ("Sliding Window (Optimal)", solution.balancedString),
        ("Counter Approach", solution.balancedString_counter),
        ("Optimized", solution.balancedString_optimized),
        ("Brute Force", solution.balancedString_brute)  # Only test on small inputs
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for s, expected in test_cases:
            # Skip brute force for very long strings
            if approach_name == "Brute Force" and len(s) > 16:
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
    
    # Detailed trace for "QQWE" 
    print("Detailed trace for 'QQWE':")
    s = "QQWE"
    n = len(s)
    target = n // 4  # = 1
    
    print(f"String: {s}, Length: {n}, Target per char: {target}")
    
    # Count frequencies
    count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
    for char in s:
        count[char] += 1
    
    print(f"Current counts: {count}")
    
    # Find excess
    excess = {}
    for char in 'QWER':
        if count[char] > target:
            excess[char] = count[char] - target
    
    print(f"Excess characters: {excess}")
    print("Need to find minimum window containing: 1 'Q'")
    
    # Trace sliding window
    left = 0
    window_count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
    min_length = n
    
    for right in range(n):
        window_count[s[right]] += 1
        print(f"Right={right}, char='{s[right]}', window={s[left:right+1]}")
        print(f"  Window count: {window_count}")
        
        # Check if valid and contract
        while all(window_count.get(char, 0) >= needed for char, needed in excess.items()):
            current_length = right - left + 1
            min_length = min(min_length, current_length)
            print(f"  Valid window '{s[left:right+1]}' length={current_length}, min_so_far={min_length}")
            
            window_count[s[left]] -= 1
            left += 1
            if left <= right:
                print(f"  Contract left to {left}, new window: '{s[left:right+1]}'")
    
    print(f"Final result: {min_length}")
    
    # Explanation
    print("\nWhy this works:")
    print("1. Count frequency of each character")
    print("2. Find 'excess' characters (those appearing > n/4 times)")  
    print("3. Use sliding window to find minimum substring containing all excess")
    print("4. Replace that substring to balance the string")