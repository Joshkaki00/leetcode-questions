# LeetCode 21: Merge Two Sorted Lists
"""
LeetCode 21: Merge Two Sorted Lists
SCENARIO: Hospital Patient Queue Management
You're developing software for a hospital's emergency department. Two separate triage stations 
evaluate patients and assign priority scores, creating two sorted lists of patients (sorted by urgency). 
When the hospital gets busy, these two queues need to be merged into a single prioritized list while 
maintaining the correct order. Lives depend on getting the most critical patients treated first, so the 
merging process must preserve the sorted order perfectly. The system must handle this efficiently even 
during peak emergency periods.
Problem:
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing 
together the nodes of the first two lists.
Args:
    list1 (ListNode): Head of the first sorted linked list
    list2 (ListNode): Head of the second sorted linked list
Returns:
    ListNode: Head of the merged sorted linked list
Time Complexity: O(m + n) where m and n are the lengths of the two lists
Space Complexity: 
    - Iterative approach: O(1) - only uses constant extra space
    - Recursive approach: O(m + n) - due to recursion stack
Examples:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    Input: list1 = [], list2 = []
    Output: []
    Input: list1 = [], list2 = [0]
    Output: [0]
Approaches:
1. Iterative with dummy node: Uses a dummy head to simplify edge cases and iteratively compares nodes
2. Recursive: Recursively chooses the smaller head and merges the rest of the lists
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Approach 1: Iterative with dummy node
    def mergeTwoLists(self, list1, list2):
        # Create dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Compare nodes from both lists and merge
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes (one list might be longer)
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # Return head of merged list (skip dummy node)
        return dummy.next
    
    # Approach 2: Recursive
    def mergeTwoLists_recursive(self, list1, list2):
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Recursive case: choose smaller head and recurse
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_recursive(list1, list2.next)
            return list2

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

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,2,4] and [1,3,4]
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 1 - Iterative: {linked_list_to_array(merged)}")
    
    # Test case 2: [] and []
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 2 - Iterative: {linked_list_to_array(merged)}")
    
    # Test case 3: [] and [0]
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 3 - Iterative: {linked_list_to_array(merged)}")
    
    # Test recursive approach
    print("\nRecursive approach:")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = solution.mergeTwoLists_recursive(list1, list2)
    print(f"Test 1 - Recursive: {linked_list_to_array(merged)}")