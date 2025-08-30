# LeetCode 28: Find the Index of the First Occurrence in a String

class Solution:
    # Approach 1: Built-in method (simplest)
    def strStr_builtin(self, haystack, needle):
        # Python's built-in find method
        result = haystack.find(needle)
        return result if result != -1 else -1
    
    # Approach 2: Brute Force (sliding window)
    def strStr(self, haystack, needle):
        # Edge case: empty needle
        if not needle:
            return 0
        
        needle_len = len(needle)
        haystack_len = len(haystack)
        
        # Check each possible starting position
        for i in range(haystack_len - needle_len + 1):
            # Check if needle matches starting at position i
            if haystack[i:i + needle_len] == needle:
                return i
        
        return -1
    
    # Approach 3: Character-by-character comparison
    def strStr_char_by_char(self, haystack, needle):
        if not needle:
            return 0
        
        needle_len = len(needle)
        haystack_len = len(haystack)
        
        # Check each possible starting position
        for i in range(haystack_len - needle_len + 1):
            # Compare character by character
            match = True
            for j in range(needle_len):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            
            if match:
                return i
        
        return -1
    
    # Approach 4: KMP Algorithm (advanced, optimal)
    def strStr_KMP(self, haystack, needle):
        if not needle:
            return 0
        
        # Build failure function (LPS array)
        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0  # length of previous longest prefix suffix
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        lps = build_lps(needle)
        i = 0  # index for haystack
        j = 0  # index for needle
        
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            
            if j == len(needle):
                return i - j  # Found match
            elif i < len(haystack) and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
        ("a", "", 0),
        ("mississippi", "issip", 4)
    ]

    print("Testing strStr (Brute Force approach):")
    for haystack, needle, expected in test_cases:
        result = solution.strStr(haystack, needle)
        status = "✓" if result == expected else "✗"
        print(f"{status} strStr('{haystack}', '{needle}') = {result} (expected: {expected})")

    print("\nTesting strStr_KMP (KMP Algorithm):")
    for haystack, needle, expected in test_cases:
        result = solution.strStr_KMP(haystack, needle)
        status = "✓" if result == expected else "✗"
        print(f"{status} strStr_KMP('{haystack}', '{needle}') = {result} (expected: {expected})")

    print("\nTesting strStr_char_by_char:")
    for haystack, needle, expected in test_cases:
        result = solution.strStr_char_by_char(haystack, needle)
        status = "✓" if result == expected else "✗"
        print(f"{status} strStr_char_by_char('{haystack}', '{needle}') = {result} (expected: {expected})")