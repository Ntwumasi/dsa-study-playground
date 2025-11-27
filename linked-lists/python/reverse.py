"""
Reverse Linked List (LeetCode 206)

PATTERN: Iterative Pointer Reversal
- Maintain three pointers: prev, curr, next
- Reverse direction of each pointer as we traverse
- prev becomes the new head

TIME COMPLEXITY: O(n) - single pass through the list
SPACE COMPLEXITY: O(1) - only three pointers

WHY THIS WORKS:
- We change each node's next pointer to point backwards
- Save next node before changing pointer (or we lose it!)
- When done, prev points to the new head (old tail)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list iteratively.

    Args:
        head: Head of the linked list

    Returns:
        Head of the reversed list

    Visual:
        Input:  [1] -> [2] -> [3] -> [4] -> [5] -> None

        Initial: prev=None, curr=1

        Step 1: Save next=2
                Reverse: 1.next = None (prev)
                Move: prev=1, curr=2
                None <- [1]    [2] -> [3] -> [4] -> [5]

        Step 2: Save next=3
                Reverse: 2.next = 1 (prev)
                Move: prev=2, curr=3
                None <- [1] <- [2]    [3] -> [4] -> [5]

        Step 3: Save next=4
                Reverse: 3.next = 2 (prev)
                Move: prev=3, curr=4
                None <- [1] <- [2] <- [3]    [4] -> [5]

        Step 4: Save next=5
                Reverse: 4.next = 3 (prev)
                Move: prev=4, curr=5
                None <- [1] <- [2] <- [3] <- [4]    [5]

        Step 5: Save next=None
                Reverse: 5.next = 4 (prev)
                Move: prev=5, curr=None
                None <- [1] <- [2] <- [3] <- [4] <- [5]

        curr is None, stop. Return prev (node 5)

        Output: [5] -> [4] -> [3] -> [2] -> [1] -> None
    """
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # Save next before we overwrite it
        curr.next = prev       # Reverse the pointer
        prev = curr            # Move prev forward
        curr = next_node       # Move curr forward

    return prev  # prev is now the new head


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a linked list recursively.

    TIME: O(n), SPACE: O(n) for recursion stack

    Visual:
        reverse([1] -> [2] -> [3])
        = reverse([2] -> [3]) with [1]
        = reverse([3]) with [2] and [1]
        = [3] with [2] and [1]
        = [3] -> [2] -> [1]
    """
    # Base case: empty or single node
    if not head or not head.next:
        return head

    # Recursively reverse the rest
    new_head = reverse_list_recursive(head.next)

    # head.next is now the last node of reversed list
    # Make it point back to head
    head.next.next = head
    head.next = None

    return new_head


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    LeetCode 92: Reverse Linked List II

    Reverse nodes from position left to right (1-indexed).

    Visual:
        Input: [1] -> [2] -> [3] -> [4] -> [5], left=2, right=4
        Output: [1] -> [4] -> [3] -> [2] -> [5]
    """
    if not head or left == right:
        return head

    # Dummy node to handle edge case where left = 1
    dummy = ListNode(0, head)
    prev = dummy

    # Move prev to node before left position
    for _ in range(left - 1):
        prev = prev.next

    # Start reversing from left position
    curr = prev.next
    for _ in range(right - left):
        # Remove next node and insert it after prev
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next


# Helper functions
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test cases
if __name__ == "__main__":
    # Example 1: Normal case
    head1 = create_list([1, 2, 3, 4, 5])
    result1 = reverse_list(head1)
    print(f"[1,2,3,4,5] reversed: {list_to_array(result1)}")  # [5,4,3,2,1]

    # Example 2: Two nodes
    head2 = create_list([1, 2])
    result2 = reverse_list(head2)
    print(f"[1,2] reversed: {list_to_array(result2)}")  # [2,1]

    # Example 3: Single node
    head3 = create_list([1])
    result3 = reverse_list(head3)
    print(f"[1] reversed: {list_to_array(result3)}")  # [1]

    # Example 4: Empty list
    result4 = reverse_list(None)
    print(f"[] reversed: {list_to_array(result4)}")  # []

    # Recursive approach
    head5 = create_list([1, 2, 3, 4, 5])
    result5 = reverse_list_recursive(head5)
    print(f"\nRecursive: {list_to_array(result5)}")  # [5,4,3,2,1]

    # Reverse between positions
    head6 = create_list([1, 2, 3, 4, 5])
    result6 = reverse_between(head6, 2, 4)
    print(f"[1,2,3,4,5] reverse(2,4): {list_to_array(result6)}")  # [1,4,3,2,5]

    """
    REVERSAL PATTERNS:

    1. Reverse entire list:
       - Iterative: O(1) space, three pointers
       - Recursive: O(n) space, elegant but uses stack

    2. Reverse between positions (LeetCode 92):
       - Find start position
       - Reverse section
       - Reconnect ends

    3. Reverse in k-groups (LeetCode 25):
       - Reverse k nodes at a time
       - Handle remaining nodes

    4. Palindrome check:
       - Find middle (fast/slow)
       - Reverse second half
       - Compare halves

    POINTER ORDER IS CRITICAL:

    WRONG:
        curr.next = prev  // Lost access to rest of list!
        prev = curr
        curr = curr.next  // curr.next is now prev, infinite loop!

    CORRECT:
        next_node = curr.next  // Save it first!
        curr.next = prev
        prev = curr
        curr = next_node

    RECURSION INSIGHT:
        The key insight for recursive reversal is that
        head.next.next = head makes the second node point back to first.
        Then head.next = None makes first node the new tail.
    """
