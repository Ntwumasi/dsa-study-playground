"""
Middle of the Linked List (LeetCode 876)

PATTERN: Fast and Slow Pointers (Floyd's Tortoise and Hare)
- Slow pointer moves 1 step at a time
- Fast pointer moves 2 steps at a time
- When fast reaches end, slow is at middle

TIME COMPLEXITY: O(n) - single pass through the list
SPACE COMPLEXITY: O(1) - only two pointers

WHY THIS WORKS:
- Fast pointer moves twice as fast as slow
- When fast travels n nodes, slow travels n/2 nodes
- So when fast reaches the end, slow is at the middle
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node of a linked list.

        If there are two middle nodes, return the second middle node.

        Args:
            head: Head of the linked list

        Returns:
            Middle node of the list

        Visual:
            Odd length: [1] -> [2] -> [3] -> [4] -> [5]

            Step 0: slow=1, fast=1
            Step 1: slow=2, fast=3
            Step 2: slow=3, fast=5
            Step 3: fast.next is None, stop

            Return: [3] (the middle)

        Even length: [1] -> [2] -> [3] -> [4] -> [5] -> [6]

            Step 0: slow=1, fast=1
            Step 1: slow=2, fast=3
            Step 2: slow=3, fast=5
            Step 3: slow=4, fast=None (fast.next.next goes past end)

            Return: [4] (second of two middles)
        """
        slow = head
        fast = head

        # Move fast 2 steps and slow 1 step
        # Loop continues while fast can move 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches end, slow is at middle
        return slow


def middle_node_array(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Alternative: Convert to array first.

    TIME: O(n), SPACE: O(n)

    Simpler but uses extra space.
    """
    nodes = []
    current = head

    while current:
        nodes.append(current)
        current = current.next

    return nodes[len(nodes) // 2]


def middle_node_two_pass(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Alternative: Two-pass approach.

    First pass counts nodes, second pass goes to middle.
    TIME: O(n), SPACE: O(1)
    """
    # First pass: count nodes
    count = 0
    current = head
    while current:
        count += 1
        current = current.next

    # Second pass: go to middle
    middle_index = count // 2
    current = head
    for _ in range(middle_index):
        current = current.next

    return current


# Helper function to create linked list from array
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Odd length
    head1 = create_list([1, 2, 3, 4, 5])
    print(f"[1,2,3,4,5] middle: {sol.middleNode(head1).val}")  # 3

    # Example 2: Even length
    head2 = create_list([1, 2, 3, 4, 5, 6])
    print(f"[1,2,3,4,5,6] middle: {sol.middleNode(head2).val}")  # 4

    # Example 3: Single node
    head3 = create_list([1])
    print(f"[1] middle: {sol.middleNode(head3).val}")  # 1

    # Example 4: Two nodes
    head4 = create_list([1, 2])
    print(f"[1,2] middle: {sol.middleNode(head4).val}")  # 2

    """
    FAST AND SLOW POINTER APPLICATIONS:

    1. Find middle of linked list (this problem)
       - Fast moves 2x, when fast at end, slow at middle

    2. Detect cycle in linked list (LeetCode 141)
       - If fast catches up to slow, there's a cycle

    3. Find start of cycle (LeetCode 142)
       - After detecting cycle, reset one pointer to head
       - Move both one step at a time until they meet

    4. Find nth node from end
       - Move fast n steps ahead, then move both together

    5. Palindrome linked list
       - Find middle, reverse second half, compare

    VISUAL OF POINTER MOVEMENT:

    List: 1 -> 2 -> 3 -> 4 -> 5 -> None

    Step 0:
    slow:  1
    fast:  1

    Step 1:
    slow:     2
    fast:        3

    Step 2:
    slow:        3
    fast:              5

    Step 3: fast.next is None, stop
    Return slow (node 3)
    """
