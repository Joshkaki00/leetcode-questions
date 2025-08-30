# LeetCode 2: Add Two Numbers

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Main approach: Simulate elementary addition with carry
    def addTwoNumbers(self, l1, l2):
        # Create dummy head to simplify list construction
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Process both lists while there are nodes or carry exists
        while l1 or l2 or carry:
            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10  # Integer division for carry
            digit = total % 10   # Remainder is the digit to store
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the actual head (skip dummy)
        return dummy_head.next
    
    # Alternative approach: More explicit handling
    def addTwoNumbers_explicit(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Process nodes while both lists have nodes
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next
            
            l1 = l1.next
            l2 = l2.next
        
        # Process remaining nodes in l1
        while l1:
            total = l1.val + carry
            carry = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next
            l1 = l1.next
        
        # Process remaining nodes in l2
        while l2:
            total = l2.val + carry
            carry = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next
            l2 = l2.next
        
        # Handle final carry if it exists
        if carry:
            current.next = ListNode(carry)
        
        return dummy_head.next

# Helper functions for testing
def create_linked_list(arr):
    """Create a linked list from an array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    """Convert linked list to array for easy display"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_number(arr):
    """Convert reversed digit array to actual number for verification"""
    return int(''.join(str(d) for d in reversed(arr))) if arr else 0

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([2, 4, 3], [5, 6, 4]),  # 342 + 465 = 807
        ([0], [0]),              # 0 + 0 = 0
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])  # 9999999 + 9999 = 10009998
    ]
    
    for i, (arr1, arr2) in enumerate(test_cases):
        l1 = create_linked_list(arr1)
        l2 = create_linked_list(arr2)
        
        result = solution.addTwoNumbers(l1, l2)
        result_arr = linked_list_to_array(result)
        
        # Verify the result
        num1 = array_to_number(arr1)
        num2 = array_to_number(arr2)
        expected_sum = num1 + num2
        actual_sum = array_to_number(result_arr)
        
        print(f"Test {i+1}:")
        print(f"  Input: {arr1} + {arr2}")
        print(f"  Numbers: {num1} + {num2} = {expected_sum}")
        print(f"  Output: {result_arr}")
        print(f"  Verification: {actual_sum} {'✓' if actual_sum == expected_sum else '✗'}")
        print()
    
    # Test edge cases
    print("Edge case tests:")
    
    # Test with different lengths
    l1 = create_linked_list([9, 9])      # 99
    l2 = create_linked_list([1])         # 1
    result = solution.addTwoNumbers(l1, l2)
    print(f"99 + 1 = {linked_list_to_array(result)} (expected: [0, 0, 1])")
    
    # Test with carry propagation
    l1 = create_linked_list([5])         # 5
    l2 = create_linked_list([5])         # 5  
    result = solution.addTwoNumbers(l1, l2)
    print(f"5 + 5 = {linked_list_to_array(result)} (expected: [0, 1])")