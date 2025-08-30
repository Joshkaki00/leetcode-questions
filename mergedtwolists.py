# LeetCode 21: Merge Two Sorted Lists

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