"""
Remove Duplicates from Sorted List (LeetCode 83)

PATTERN: In-Place List Modification
- Traverse sorted list and skip duplicate nodes
- Connect current node directly to next non-duplicate

TIME COMPLEXITY: O(n) - single pass through the list
SPACE COMPLEXITY: O(1) - modify list in place

WHY THIS WORKS:
- List is sorted, so duplicates are adjacent
- When we find a duplicate, skip it by updating pointers
- No need to actually delete nodes (they become unreachable)
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove all duplicate nodes from sorted list (keep one copy).

        Args:
            head: Head of sorted linked list

        Returns:
            Head of list with duplicates removed

        Visual:
            Input:  [1] -> [1] -> [2] -> [3] -> [3]

            Step 1: current = 1
                    current.val == current.next.val (1 == 1)
                    Skip: current.next = current.next.next
                    List: [1] -> [2] -> [3] -> [3]

            Step 2: current = 1
                    current.val != current.next.val (1 != 2)
                    Move: current = current.next
                    current = 2

            Step 3: current = 2
                    current.val != current.next.val (2 != 3)
                    Move: current = current.next
                    current = 3

            Step 4: current = 3
                    current.val == current.next.val (3 == 3)
                    Skip: current.next = current.next.next (None)
                    List: [1] -> [2] -> [3]

            Output: [1] -> [2] -> [3]
        """
        current = head

        while current is not None and current.next is not None:
            if current.next.val == current.val:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to next node
                current = current.next

        return head


def delete_all_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    LeetCode 82: Remove ALL nodes that have duplicates (keep none).

    Uses a dummy node to handle edge case where head is a duplicate.

    Visual:
        Input:  [1] -> [2] -> [3] -> [3] -> [4] -> [4] -> [5]
        Output: [1] -> [2] -> [5]
        (All 3s and 4s removed completely)
    """
    # Dummy node to handle edge case where head is duplicate
    dummy = ListNode(0, head)
    prev = dummy

    while head:
        # If current node is start of duplicates
        if head.next and head.val == head.next.val:
            # Skip all nodes with this value
            while head.next and head.val == head.next.val:
                head = head.next
            # Skip the last duplicate too
            prev.next = head.next
        else:
            # No duplicate, move prev forward
            prev = prev.next

        head = head.next

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
    sol = Solution()

    # Example 1
    head1 = create_list([1, 1, 2])
    result1 = sol.deleteDuplicates(head1)
    print(f"[1,1,2] -> {list_to_array(result1)}")  # [1, 2]

    # Example 2
    head2 = create_list([1, 1, 2, 3, 3])
    result2 = sol.deleteDuplicates(head2)
    print(f"[1,1,2,3,3] -> {list_to_array(result2)}")  # [1, 2, 3]

    # Example 3: No duplicates
    head3 = create_list([1, 2, 3])
    result3 = sol.deleteDuplicates(head3)
    print(f"[1,2,3] -> {list_to_array(result3)}")  # [1, 2, 3]

    # Example 4: All same
    head4 = create_list([1, 1, 1, 1])
    result4 = sol.deleteDuplicates(head4)
    print(f"[1,1,1,1] -> {list_to_array(result4)}")  # [1]

    # LeetCode 82: Remove ALL duplicates
    print("\nLeetCode 82 - Remove ALL duplicates:")
    head5 = create_list([1, 2, 3, 3, 4, 4, 5])
    result5 = delete_all_duplicates(head5)
    print(f"[1,2,3,3,4,4,5] -> {list_to_array(result5)}")  # [1, 2, 5]

    """
    LINKED LIST DELETION PATTERNS:

    1. Delete specific value:
       - Traverse and skip nodes with target value
       - Use dummy node if head might be deleted

    2. Delete duplicates (keep one):
       - Compare current with next
       - Skip if same value

    3. Delete ALL duplicates (keep none):
       - Need to detect ALL occurrences first
       - Use prev pointer to skip entire sequence

    4. Delete nth node from end:
       - Use two pointers, n apart
       - When fast reaches end, slow is at target

    KEY INSIGHT FOR SORTED LISTS:
    - Duplicates are always adjacent
    - Single pass is sufficient
    - No need for hash set to track seen values

    DUMMY NODE TECHNIQUE:
    - Create dummy node before head
    - Simplifies edge cases (deleting head)
    - Return dummy.next at the end
    """
