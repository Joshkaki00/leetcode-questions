# LeetCode 5: Longest Palindromic Substring

class Solution:
    # Approach 1: Brute Force - Check all substrings
    def longestPalindrome_brute(self, s):
        def is_palindrome(string):
            return string == string[::-1]
        
        n = len(s)
        longest = ""
        
        # Check all possible substrings
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring
        
        return longest
    
    # Approach 2: Expand Around Centers (optimal for this problem)
    def longestPalindrome(self, s):
        def expand_around_center(left, right):
            # Expand while characters match and within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindrome (before the mismatch)
            return s[left + 1:right]
        
        longest = ""
        
        for i in range(len(s)):
            # Check for odd-length palindromes (center at i)
            palindrome1 = expand_around_center(i, i)
            
            # Check for even-length palindromes (center between i and i+1)
            palindrome2 = expand_around_center(i, i + 1)
            
            # Update longest if we found a longer palindrome
            for palindrome in [palindrome1, palindrome2]:
                if len(palindrome) > len(longest):
                    longest = palindrome
        
        return longest
    
    # Approach 3: Dynamic Programming
    def longestPalindrome_dp(self, s):
        n = len(s)
        if n <= 1:
            return s
        
        # dp[i][j] represents whether substring s[i:j+1] is palindrome
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
        
        # Check for palindromes of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # ending index
                
                # Check if s[i:j+1] is palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        
        return s[start:start + max_len]
    
    # Approach 4: Manacher's Algorithm (most advanced, O(n))
    def longestPalindrome_manacher(self, s):
        # Preprocess: insert '#' between characters
        # "babad" becomes "#b#a#b#a#d#"
        processed = '#'.join('^{}$'.format(s))
        n = len(processed)
        
        # Array to store radius of palindrome at each position
        radius = [0] * n
        center = 0  # center of rightmost palindrome
        right = 0   # right boundary of rightmost palindrome
        
        max_len = 0
        center_index = 0
        
        for i in range(1, n - 1):
            # Mirror of i with respect to center
            mirror = 2 * center - i
            
            # If i is within right boundary, we can use previously computed values
            if i < right:
                radius[i] = min(right - i, radius[mirror])
            
            # Try to expand palindrome centered at i
            while processed[i + radius[i] + 1] == processed[i - radius[i] - 1]:
                radius[i] += 1
            
            # If palindrome centered at i extends past right, adjust center and right
            if i + radius[i] > right:
                center = i
                right = i + radius[i]
            
            # Update maximum length palindrome
            if radius[i] > max_len:
                max_len = radius[i]
                center_index = i
        
        # Extract the longest palindrome
        start = (center_index - max_len) // 2
        return s[start:start + max_len]

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        "babad",      # Expected: "bab" or "aba"
        "cbbd",       # Expected: "bb"
        "a",          # Expected: "a"
        "ac",         # Expected: "a" or "c"
        "racecar",    # Expected: "racecar"
        "noon",       # Expected: "noon"
        "abcdef",     # Expected: "a" (or any single char)
        "aabbaa"      # Expected: "aabbaa"
    ]
    
    print("Testing longestPalindrome (Expand Around Centers):")
    for s in test_cases:
        result = solution.longestPalindrome(s)
        print(f"longestPalindrome('{s}') = '{result}'")
    
    print("\nTesting longestPalindrome_dp (Dynamic Programming):")
    for s in test_cases:
        result = solution.longestPalindrome_dp(s)
        print(f"longestPalindrome_dp('{s}') = '{result}'")
    
    print("\nTesting longestPalindrome_manacher (Manacher's Algorithm):")
    for s in test_cases:
        result = solution.longestPalindrome_manacher(s)
        print(f"longestPalindrome_manacher('{s}') = '{result}'")