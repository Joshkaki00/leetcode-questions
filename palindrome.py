# LeetCode 9: Palindrome Number

class Solution:
    # Approach 1: String Conversion (Straightforward)
    def isPalindrome_string(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Convert to string and check if it equals its reverse
        s = str(x)
        return s == s[::-1]

    # Approach 2: Mathematical (Follow-up - no string conversion)
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Single digit numbers are palindromes
        if x < 10:
            return True

        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x % 10 == 0:
            return False

        # Reverse half of the number
        original = x
        reversed_half = 0

        # Continue until we've processed half the digits
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even number of digits: x == reversed_half
        # For odd number of digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [121, -121, 10, 0, 12321, 1221]

    print("Testing isPalindrome (Mathematical approach):")
    for num in test_cases:
        result = solution.isPalindrome(num)
        print(f"isPalindrome({num}) = {result}")

    print("\nTesting isPalindrome_string (String approach):")
    for num in test_cases:
        result = solution.isPalindrome_string(num)
        print(f"isPalindrome_string({num}) = {result}")
