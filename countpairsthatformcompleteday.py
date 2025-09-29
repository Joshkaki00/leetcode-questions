# LeetCode 3184: Count Pairs That Form a Complete Day I

# SCENARIO: Employee Shift Scheduling System
# You're developing a workforce management system for a 24/7 call center. The system
# tracks how many hours each employee has worked, and you need to identify pairs of
# employees whose combined hours equal complete 24-hour days (or multiples of 24).
# This is important for scheduling purposes - when two employees' hours sum to a
# complete day cycle, they can be paired for complementary shift coverage. For example,
# one employee worked 12 hours and another worked 12 hours - together they cover a
# full 24-hour day. Or one worked 30 hours and another worked 18 hours - together
# that's 48 hours (2 complete days). Your system needs to count all such valid pairings
# to optimize shift assignments and ensure balanced workload distribution across the team.

class Solution:
    # Approach 1: Brute Force - Check All Pairs
    def countCompleteDayPairs(self, hours):
        """
        Check every possible pair (i, j) where i < j.
        Simple but inefficient for large arrays.
        """
        count = 0
        n = len(hours)
        
        # Check all pairs where i < j
        for i in range(n):
            for j in range(i + 1, n):
                # Check if sum is divisible by 24
                if (hours[i] + hours[j]) % 24 == 0:
                    count += 1
        
        return count
    
    # Approach 2: Hash Map with Modulo (Optimal)
    def countCompleteDayPairs_optimal(self, hours):
        """
        Use modulo arithmetic and hash map to find complements.
        Key insight: (a + b) % 24 == 0 means a % 24 + b % 24 = 24 (or 0)
        """
        count = 0
        remainder_count = {}
        
        for hour in hours:
            # Calculate remainder when divided by 24
            remainder = hour % 24
            
            # Find complement: what remainder do we need to make 24?
            # If remainder is 0, we need another 0
            # If remainder is x, we need (24 - x)
            if remainder == 0:
                complement = 0
            else:
                complement = 24 - remainder
            
            # If complement exists in map, we found valid pairs
            if complement in remainder_count:
                count += remainder_count[complement]
            
            # Add current remainder to map
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        
        return count
    
    # Approach 3: Array-based Counting (Most Efficient)
    def countCompleteDayPairs_array(self, hours):
        """
        Use fixed-size array since remainders are 0-23.
        Slightly faster than hash map due to direct array access.
        """
        count = 0
        remainder_freq = [0] * 24  # Remainders can only be 0-23
        
        for hour in hours:
            remainder = hour % 24
            
            # Find complement
            if remainder == 0:
                # Need another 0 to sum to 24 (or 0)
                count += remainder_freq[0]
            else:
                # Need (24 - remainder) to sum to 24
                count += remainder_freq[24 - remainder]
            
            # Update frequency
            remainder_freq[remainder] += 1
        
        return count
    
    # Approach 4: Modulo with Detailed Tracking (Educational)
    def countCompleteDayPairs_verbose(self, hours):
        """
        Same as optimal but with detailed tracking for understanding.
        """
        count = 0
        remainder_map = {}
        pairs_found = []  # Track which pairs we found
        
        for i, hour in enumerate(hours):
            remainder = hour % 24
            complement = (24 - remainder) % 24  # Handles 0 case elegantly
            
            if complement in remainder_map:
                # Found pairs - add count
                count += remainder_map[complement]
                # Track pairs for visualization
                for prev_idx in remainder_map[complement]:
                    pairs_found.append((prev_idx, i))
            
            # Store index with this remainder
            if remainder not in remainder_map:
                remainder_map[remainder] = []
            remainder_map[remainder].append(i)
        
        return count

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([12, 12, 30, 24, 24], 2),      # Example 1: (0,1) and (3,4)
        ([72, 48, 24, 3], 3),           # Example 2: (0,1), (0,2), (1,2)
        ([24, 24, 24], 3),              # All same, all pairs work
        ([1, 23, 2, 22], 2),            # (0,1) and (2,3)
        ([5, 19, 10, 14], 2),           # (0,1) and (2,3)
        ([12], 0),                      # Single element, no pairs
        ([1, 2, 3], 0),                 # No valid pairs
        ([24], 0),                      # Single 24
        ([0, 24, 48], 3),               # All multiples of 24
        ([13, 11, 25, 23], 2)           # 13+11=24, 25+23=48
    ]
    
    approaches = [
        ("Brute Force", solution.countCompleteDayPairs),
        ("Hash Map (Optimal)", solution.countCompleteDayPairs_optimal),
        ("Array Counting", solution.countCompleteDayPairs_array),
        ("Verbose Tracking", solution.countCompleteDayPairs_verbose)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for hours, expected in test_cases:
            result = method(hours)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} hours={hours} → {result} (expected: {expected})")
            else:
                print(f"  {status} hours={hours} → {result}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed walkthrough for Example 1
    print("Detailed walkthrough for Example 1: hours=[12,12,30,24,24]")
    hours = [12, 12, 30, 24, 24]
    print(f"Array: {hours}")
    print()
    
    print("Step-by-step with Hash Map approach:")
    remainder_count = {}
    count = 0
    
    for i, hour in enumerate(hours):
        remainder = hour % 24
        complement = (24 - remainder) % 24
        
        print(f"Index {i}: hour={hour}")
        print(f"  Remainder: {hour} % 24 = {remainder}")
        print(f"  Need complement: {complement} to make sum divisible by 24")
        
        if complement in remainder_count:
            pairs = remainder_count[complement]
            count += pairs
            print(f"  Found {pairs} previous hour(s) with remainder {complement}")
            print(f"  Total pairs so far: {count}")
        else:
            print(f"  No previous hours with remainder {complement}")
        
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        print(f"  Updated map: {remainder_count}")
        print()
    
    print(f"Final count: {count}")
    print()
    
    # Show the math behind modulo arithmetic
    print("Why modulo arithmetic works:")
    print("For (a + b) % 24 == 0 to be true:")
    print("  a % 24 + b % 24 must equal 0 or 24 or 48...")
    print("  Essentially: (a % 24) + (b % 24) ≡ 0 (mod 24)")
    print()
    print("Examples from array:")
    print(f"  hours[0]=12, hours[1]=12: (12+12) % 24 = {(12+12) % 24} ✓")
    print(f"  hours[3]=24, hours[4]=24: (24+24) % 24 = {(24+24) % 24} ✓")
    print(f"  hours[0]=12, hours[2]=30: (12+30) % 24 = {(12+30) % 24} ✗")
    print()
    
    print("Key Insights:")
    print("1. Use modulo 24 to normalize all hours to 0-23 range")
    print("2. For each hour, find complement: (24 - remainder) % 24")
    print("3. Count how many previous hours have that complement")
    print("4. This avoids checking all O(n²) pairs - reduces to O(n)")