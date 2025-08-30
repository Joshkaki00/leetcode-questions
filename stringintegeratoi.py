# LeetCode 8: String to Integer (atoi)

class Solution:
    def myAtoi(self, s):
        # Define 32-bit signed integer bounds
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   #  2147483647
        
        # Step 1: Handle empty string
        if not s:
            return 0
        
        i = 0
        n = len(s)
        
        # Step 2: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Check if we've reached end after skipping whitespaces
        if i == n:
            return 0
        
        # Step 3: Determine sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Step 4: Convert digits and handle overflow
        result = 0
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before actually adding the digit
            # If result > (INT_MAX - digit) // 10, then result * 10 + digit > INT_MAX
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        # Apply sign and return
        result *= sign
        
        # Final bounds check (though overflow should be handled above)
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result
    
    # Alternative approach with more explicit overflow handling
    def myAtoi_explicit(self, s):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        if not s:
            return 0
        
        # Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0
        
        # Check sign
        sign = 1
        start_idx = 0
        if s[0] == '-':
            sign = -1
            start_idx = 1
        elif s[0] == '+':
            start_idx = 1
        
        # Convert digits
        result = 0
        for i in range(start_idx, len(s)):
            if not s[i].isdigit():
                break
            
            digit = int(s[i])
            
            # Check overflow before multiplication
            if result > INT_MAX // 10:
                return INT_MAX if sign == 1 else INT_MIN
            elif result == INT_MAX // 10:
                if sign == 1 and digit > INT_MAX % 10:
                    return INT_MAX
                elif sign == -1 and digit > -(INT_MIN % 10):
                    return INT_MIN
            
            result = result * 10 + digit
        
        return sign * result

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("42", 42),
        ("   -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
        ("", 0),
        ("   ", 0),
        ("+1", 1),
        ("+-12", 0),
        ("21474836460", 2147483647),  # Overflow case
        ("-91283472332", -2147483648),  # Underflow case
        ("2147483647", 2147483647),   # INT_MAX
        ("-2147483648", -2147483648), # INT_MIN
        ("2147483648", 2147483647),   # Just over INT_MAX
        ("-2147483649", -2147483648), # Just under INT_MIN
        ("  0000000000012345678", 12345678),
        ("00000-42a1234", 0),
        ("   +0 123", 0)
    ]
    
    print("Testing myAtoi:")
    for s, expected in test_cases:
        result = solution.myAtoi(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} myAtoi('{s}') = {result} (expected: {expected})")
    
    print("\nTesting edge cases:")
    
    # Test with very long number strings
    long_positive = "1" * 50
    result = solution.myAtoi(long_positive)
    print(f"Long positive number: {result} (should be {2**31 - 1})")
    
    long_negative = "-" + "1" * 50
    result = solution.myAtoi(long_negative)
    print(f"Long negative number: {result} (should be {-2**31})")
    
    # Test leading zeros
    result = solution.myAtoi("000000000000000000000000000000000000000000123")
    print(f"Leading zeros: {result} (should be 123)")
    
    print("\nBoundary values:")
    print(f"INT_MAX = {2**31 - 1}")
    print(f"INT_MIN = {-2**31}")
    
    # Test boundary cases
    boundary_tests = [
        "2147483647",    # Exactly INT_MAX
        "2147483648",    # INT_MAX + 1
        "-2147483648",   # Exactly INT_MIN  
        "-2147483649"    # INT_MIN - 1
    ]
    
    for test in boundary_tests:
        result = solution.myAtoi(test)
        print(f"myAtoi('{test}') = {result}")