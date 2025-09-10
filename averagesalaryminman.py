# LeetCode 1491: Average Salary Excluding the Minimum and Maximum Salary

class Solution:
    # Approach 1: Using built-in min/max functions (Optimal)
    def average(self, salary):
        min_salary = min(salary)
        max_salary = max(salary)
        total_sum = sum(salary)
        
        # Remove min and max from total, divide by remaining count
        remaining_sum = total_sum - min_salary - max_salary
        remaining_count = len(salary) - 2
        
        # Use float() to ensure proper floating-point division
        return float(remaining_sum) / remaining_count
    
    # Approach 2: Single pass to find min/max (More efficient)
    def average_single_pass(self, salary):
        min_salary = float('inf')
        max_salary = float('-inf')
        total_sum = 0
        
        # Find min, max, and sum in single pass
        for sal in salary:
            total_sum += sal
            min_salary = min(min_salary, sal)
            max_salary = max(max_salary, sal)
        
        # Calculate average excluding min and max
        remaining_sum = total_sum - min_salary - max_salary
        remaining_count = len(salary) - 2
        
        return remaining_sum / remaining_count
    
    # Approach 3: Sorting approach (Less efficient but clear)
    def average_sorting(self, salary):
        salary.sort()
        
        # After sorting: first is min, last is max
        # Sum middle elements
        middle_sum = sum(salary[1:-1])
        middle_count = len(salary) - 2
        
        return middle_sum / middle_count
    
    # Approach 4: Manual min/max finding (Explicit)
    def average_manual(self, salary):
        if len(salary) < 3:
            return 0.0  # Edge case (though problem guarantees length >= 3)
        
        min_salary = salary[0]
        max_salary = salary[0]
        total_sum = 0
        
        # Find min, max, and sum
        for sal in salary:
            total_sum += sal
            if sal < min_salary:
                min_salary = sal
            if sal > max_salary:
                max_salary = sal
        
        return (total_sum - min_salary - max_salary) / (len(salary) - 2)
    
    # Approach 5: Using list comprehension (Pythonic)
    def average_comprehension(self, salary):
        min_sal = min(salary)
        max_sal = max(salary)
        
        # Filter out min and max, then calculate average
        filtered_salaries = [sal for sal in salary if sal != min_sal and sal != max_sal]
        
        return sum(filtered_salaries) / len(filtered_salaries)
    
    # Approach 6: Mathematical optimization (Avoid division)
    def average_optimized(self, salary):
        # For better precision, we can rearrange the calculation
        total = sum(salary)
        min_sal = min(salary)
        max_sal = max(salary)
        
        # Return as float to ensure floating point division
        return float(total - min_sal - max_sal) / (len(salary) - 2)

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([4000, 3000, 1000, 2000], 2500.0),     # Example 1
        ([1000, 2000, 3000], 2000.0),           # Example 2
        ([6000, 5000, 4000, 3000, 2000, 1000], 4000.0),  # Larger array
        ([8000, 9000, 2000, 3000, 6000, 1000], 5250.0),  # Mixed order
        ([48000, 59000, 99000, 13000, 78000, 45000, 31000, 17000, 39000, 37000, 93000, 77000, 33000, 28000, 4000, 54000, 67000, 6000, 1000, 11000], 740000/18),  # Large case - exact fraction
    ]
    
    approaches = [
        ("Built-in Min/Max", solution.average),
        ("Single Pass", solution.average_single_pass),
        ("Sorting", solution.average_sorting),
        ("Manual", solution.average_manual),
        ("List Comprehension", solution.average_comprehension),
        ("Optimized", solution.average_optimized)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for salary, expected in test_cases:
            # Make a copy since sorting approach modifies the list
            salary_copy = salary.copy()
            result = method(salary_copy)
            
            # Check if within acceptable tolerance (10^-5)
            tolerance = 1e-5
            is_correct = abs(result - expected) < tolerance
            status = "✓" if is_correct else "✗"
            
            if not is_correct:
                all_correct = False
                print(f"  {status} {salary} → {result:.5f} (expected: {expected:.5f})")
            else:
                print(f"  {status} {salary} → {result:.5f}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed walkthrough for Example 1
    print("Detailed walkthrough for [4000, 3000, 1000, 2000]:")
    salary = [4000, 3000, 1000, 2000]
    
    print(f"Original array: {salary}")
    
    # Step by step calculation
    min_salary = min(salary)
    max_salary = max(salary)
    total_sum = sum(salary)
    
    print(f"Minimum salary: {min_salary}")
    print(f"Maximum salary: {max_salary}")
    print(f"Total sum: {total_sum}")
    
    remaining_sum = total_sum - min_salary - max_salary
    remaining_count = len(salary) - 2
    average_result = remaining_sum / remaining_count
    
    print(f"Sum excluding min/max: {total_sum} - {min_salary} - {max_salary} = {remaining_sum}")
    print(f"Count excluding min/max: {len(salary)} - 2 = {remaining_count}")
    print(f"Average: {remaining_sum} / {remaining_count} = {average_result}")
    
    # Show which salaries are included
    included_salaries = [sal for sal in salary if sal != min_salary and sal != max_salary]
    print(f"Salaries included in average: {included_salaries}")
    print(f"Verification: sum({included_salaries}) / {len(included_salaries)} = {sum(included_salaries) / len(included_salaries)}")
    
    print("\nComplexity Analysis:")
    print("Built-in approach: O(n) time for min(), O(n) for max(), O(n) for sum() = O(3n) = O(n)")
    print("Single pass approach: O(n) time with only one traversal")
    print("Sorting approach: O(n log n) time due to sorting")
    print("All approaches use O(1) extra space (except sorting which may use O(n) for sorting)")