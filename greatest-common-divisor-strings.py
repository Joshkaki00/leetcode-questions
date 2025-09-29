# LeetCode 1071: Greatest Common Divisor of Strings

# SCENARIO: DNA Sequence Pattern Analysis for Genetic Research
# You're working in a bioinformatics lab analyzing repetitive DNA sequences. Scientists
# have discovered two DNA strands that appear to be composed of repeated base patterns.
# Your task is to find the largest repeating pattern (motif) that divides both sequences
# perfectly - meaning each strand is made up of this pattern repeated multiple times.
# For example, if one strand is "ATGATGATG" and another is "ATGATG", the common divisor
# pattern is "ATG" (repeated 3 times in the first, 2 times in the second). This analysis
# helps identify conserved genetic sequences that may have functional significance in
# gene regulation or protein coding. Your algorithm must quickly process thousands of
# sequence pairs to help researchers identify these meaningful biological patterns.

class Solution:
    # Approach 1: GCD of Lengths with Validation (Optimal)
    def gcdOfStrings(self, str1, str2):
        """
        Key insight: If a common divisor exists, the GCD of their lengths
        gives us the length of the largest common divisor string.
        """
        # Quick check: if concatenations don't match, no common divisor
        if str1 + str2 != str2 + str1:
            return ""
        
        # Calculate GCD manually for compatibility
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_length = gcd(len(str1), len(str2))
        
        # Return prefix of that length
        return str1[:gcd_length]
    
    # Approach 2: Brute Force Check All Possible Divisors
    def gcdOfStrings_brute(self, str1, str2):
        """
        Try all possible divisor lengths from longest to shortest.
        """
        def divides(s, t):
            """Check if string t divides string s"""
            if len(s) % len(t) != 0:
                return False
            
            # Check if s is made of repeated t
            repetitions = len(s) // len(t)
            return t * repetitions == s
        
        # Try all possible lengths from min length down to 1
        min_len = min(len(str1), len(str2))
        
        for length in range(min_len, 0, -1):
            # Check if this length divides both string lengths
            if len(str1) % length == 0 and len(str2) % length == 0:
                # Extract candidate divisor
                candidate = str1[:length]
                
                # Check if it divides both strings
                if divides(str1, candidate) and divides(str2, candidate):
                    return candidate
        
        return ""
    
    # Approach 3: Iterative GCD Calculation
    def gcdOfStrings_iterative(self, str1, str2):
        """
        Calculate GCD without using math.gcd for educational purposes.
        """
        # Check if common divisor can exist
        if str1 + str2 != str2 + str1:
            return ""
        
        # Calculate GCD using Euclidean algorithm
        def gcd_manual(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_len = gcd_manual(len(str1), len(str2))
        return str1[:gcd_len]
    
    # Approach 4: Recursive with Pattern Matching
    def gcdOfStrings_recursive(self, str1, str2):
        """
        Use recursion similar to Euclidean algorithm for numbers.
        """
        # Base case: if strings are equal, that's the GCD
        if str1 == str2:
            return str1
        
        # Make sure str1 is longer
        if len(str1) < len(str2):
            return self.gcdOfStrings_recursive(str2, str1)
        
        # If str1 doesn't start with str2, no common divisor
        if not str1.startswith(str2):
            return ""
        
        # Remove one occurrence of str2 from str1 and recurse
        return self.gcdOfStrings_recursive(str1[len(str2):], str2)

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("ABCABC", "ABC", "ABC"),           # Example 1: ABC divides both
        ("ABABAB", "ABAB", "AB"),           # Example 2: AB divides both
        ("LEET", "CODE", ""),               # Example 3: no common divisor
        ("ABCDEF", "ABC", ""),              # No division
        ("AAAA", "AA", "AA"),               # Simple repetition
        ("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXX"),
        ("ABABABAB", "ABAB", "ABAB"),       # str2 is the answer
        ("AAA", "A", "A"),                  # Single character
        ("AB", "BA", ""),                   # Different order
        ("AAAAAA", "AAA", "AAA")            # Multiple A's
    ]
    
    approaches = [
        ("GCD of Lengths (Optimal)", solution.gcdOfStrings),
        ("Brute Force", solution.gcdOfStrings_brute),
        ("Iterative GCD", solution.gcdOfStrings_iterative),
        ("Recursive", solution.gcdOfStrings_recursive)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for str1, str2, expected in test_cases:
            result = method(str1, str2)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} str1='{str1}', str2='{str2}' → '{result}' (expected: '{expected}')")
            else:
                # Shorten display for long strings
                s1 = str1 if len(str1) <= 15 else str1[:12] + "..."
                s2 = str2 if len(str2) <= 15 else str2[:12] + "..."
                print(f"  {status} str1='{s1}', str2='{s2}' → '{result}'")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed walkthrough for Example 2
    print("Detailed walkthrough for Example 2: str1='ABABAB', str2='ABAB'")
    str1 = "ABABAB"
    str2 = "ABAB"
    
    print(f"str1 = '{str1}' (length {len(str1)})")
    print(f"str2 = '{str2}' (length {len(str2)})")
    print()
    
    # Check concatenation property
    concat1 = str1 + str2
    concat2 = str2 + str1
    print("Concatenation check (necessary condition):")
    print(f"  str1 + str2 = '{concat1}'")
    print(f"  str2 + str1 = '{concat2}'")
    print(f"  Equal? {concat1 == concat2} {'✓' if concat1 == concat2 else '✗'}")
    print()
    
    # Calculate GCD
    from math import gcd
    gcd_len = gcd(len(str1), len(str2))
    print(f"GCD of lengths:")
    print(f"  GCD({len(str1)}, {len(str2)}) = {gcd_len}")
    print()
    
    # Extract result
    result = str1[:gcd_len]
    print(f"Result: first {gcd_len} characters of str1 = '{result}'")
    print()
    
    # Verify
    print("Verification:")
    print(f"  str1 '{str1}' = '{result}' × {len(str1)//gcd_len} = '{result * (len(str1)//gcd_len)}' ✓")
    print(f"  str2 '{str2}' = '{result}' × {len(str2)//gcd_len} = '{result * (len(str2)//gcd_len)}' ✓")
    print()
    
    # Explain why GCD works
    print("Why GCD of lengths works:")
    print("1. If both strings are made of pattern P repeated:")
    print("   - str1 = P × a (P repeated a times)")
    print("   - str2 = P × b (P repeated b times)")
    print("2. Then len(str1) = len(P) × a")
    print("        len(str2) = len(P) × b")
    print("3. GCD(len(str1), len(str2)) = len(P) × GCD(a, b)")
    print("4. The largest P has length = GCD(len(str1), len(str2)) / GCD(a,b)")
    print("5. But since P must divide both, it's length is GCD(len(str1), len(str2))")
    print()
    
    print("Key Insights:")
    print("1. Concatenation check: str1+str2 == str2+str1 proves common pattern exists")
    print("2. GCD of lengths gives us the exact length of largest common divisor")
    print("3. Time complexity: O(n + m) for string operations + O(log(min(n,m))) for GCD")
    print("4. This is much faster than checking all possible divisor lengths")