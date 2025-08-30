# LeetCode 13: Roman to Integer

class Solution:
    # Approach 1: Handle subtraction cases explicitly
    def romanToInt_explicit(self, s):
        # Map Roman symbols to values
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        # Map subtraction cases
        subtraction_cases = {
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }

        total = 0
        i = 0

        while i < len(s):
            # Check if current position forms a subtraction case
            if i + 1 < len(s) and s[i:i+2] in subtraction_cases:
                total += subtraction_cases[s[i:i+2]]
                i += 2  # Skip next character since we processed 2 characters
            else:
                total += values[s[i]]
                i += 1

        return total

    # Approach 2: Reverse iteration (clever solution)
    def romanToInt(self, s):
        # Map Roman symbols to values
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        # Iterate from right to left
        for i in range(len(s) - 1, -1, -1):
            current_value = values[s[i]]

            # If current value is smaller than previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value

        return total

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    test_cases = ["III", "LVIII", "MCMXCIV", "IV", "IX", "XL", "XC", "CD", "CM"]
    expected = [3, 58, 1994, 4, 9, 40, 90, 400, 900]

    print("Testing romanToInt (Reverse iteration approach):")
    for i, roman in enumerate(test_cases):
        result = solution.romanToInt(roman)
        print(f"romanToInt('{roman}') = {result} (expected: {expected[i]})")

    print("\nTesting romanToInt_explicit (Explicit subtraction approach):")
    for i, roman in enumerate(test_cases):
        result = solution.romanToInt_explicit(roman)
        print(f"romanToInt_explicit('{roman}') = {result} (expected: {expected[i]})")
