# Linked Lists

## When to Use
- Dynamic size requirements
- Frequent insertions/deletions at arbitrary positions
- No need for random access
- Implementing stacks, queues, graphs

## Visual

### Singly Linked List Structure
```
head
  ↓
┌───┬───┐   ┌───┬───┐   ┌───┬───┐   ┌───┬───┐
│ 1 │ ──┼──→│ 2 │ ──┼──→│ 3 │ ──┼──→│ 4 │ ──┼──→ null
└───┴───┘   └───┴───┘   └───┴───┘   └───┴───┘
 val  next   val  next   val  next   val  next
```

### Reverse Linked List
```
Original:  1 → 2 → 3 → 4 → null

Step 1:    null ← 1    2 → 3 → 4 → null
           prev  curr  next

Step 2:    null ← 1 ← 2    3 → 4 → null
                 prev curr next

Step 3:    null ← 1 ← 2 ← 3    4 → null
                      prev curr next

Step 4:    null ← 1 ← 2 ← 3 ← 4
                           prev curr

Result:    4 → 3 → 2 → 1 → null
```

### Find Middle (Fast & Slow Pointers)
```
List: 1 → 2 → 3 → 4 → 5

      S
      F
      1 → 2 → 3 → 4 → 5

          S
              F
      1 → 2 → 3 → 4 → 5

              S
                      F
      1 → 2 → 3 → 4 → 5

Slow at middle (3) when Fast reaches end!
```

### Detect Cycle (Floyd's Algorithm)
```
      1 → 2 → 3
              ↓
          6 ← 5 ← 4
          ↓
          └──────┘

Fast moves 2 steps, Slow moves 1 step
If they meet → cycle exists!

Step 1: S=1, F=1
Step 2: S=2, F=3
Step 3: S=3, F=5
Step 4: S=4, F=4  ← They meet! Cycle detected.
```

## Template

### Python
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reverse linked list
def reverse(head):
    prev = None
    curr = head

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    return prev

# Find middle
def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Detect cycle
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# Remove duplicates from sorted list
def remove_duplicates(head):
    curr = head

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head

# Merge two sorted lists
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2
    return dummy.next
```

### TypeScript
```typescript
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val = 0, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

// Reverse linked list
function reverse(head: ListNode | null): ListNode | null {
  let prev: ListNode | null = null;
  let curr = head;

  while (curr) {
    const nextTemp = curr.next;
    curr.next = prev;
    prev = curr;
    curr = nextTemp;
  }

  return prev;
}

// Find middle
function findMiddle(head: ListNode | null): ListNode | null {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow!.next;
    fast = fast.next.next;
  }

  return slow;
}

// Detect cycle
function hasCycle(head: ListNode | null): boolean {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow!.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }

  return false;
}
```

## Complexity
- **Access:** O(n) - must traverse
- **Insert/Delete at head:** O(1)
- **Insert/Delete at position:** O(n)
- **Space:** O(n)

## Common Problems
- [x] Reverse Linked List
- [x] Middle of Linked List
- [x] Remove Duplicates
- [ ] Linked List Cycle
- [ ] Merge Two Sorted Lists
- [ ] Remove Nth Node From End
- [ ] Palindrome Linked List
