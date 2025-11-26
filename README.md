# DSA Study Playground

A hands-on repository for learning Data Structures and Algorithms with solutions in **Python** and **TypeScript**.

## Structure

```
dsa-study-playground/
├── arrays-and-strings/
│   ├── two-pointer/          # Opposite & same direction patterns
│   ├── sliding-window/       # Fixed & dynamic window patterns
│   ├── prefix-sum/           # Cumulative sum techniques
│   └── misc/
├── hash-maps/                # Frequency counting, lookups
├── stacks-and-queues/        # LIFO/FIFO patterns
├── trees/                    # Traversals, BST, recursion
├── binary-search/            # Search space reduction
├── dynamic-programming/      # Memoization & tabulation
└── cheat-sheets/             # Quick reference
```

## Learning Roadmap

### Phase 1: Fundamentals
1. **Arrays & Strings**
   - [ ] Two Pointer technique
   - [ ] Sliding Window
   - [ ] Prefix Sum

2. **Hash Maps**
   - [ ] Frequency counting
   - [ ] Two Sum pattern

### Phase 2: Linear Structures
3. **Stacks & Queues**
   - [ ] Valid parentheses
   - [ ] Monotonic stack

### Phase 3: Non-Linear Structures
4. **Trees**
   - [ ] DFS traversals (in/pre/post-order)
   - [ ] BFS (level-order)
   - [ ] BST operations

5. **Binary Search**
   - [ ] Basic search
   - [ ] Boundary finding
   - [ ] Rotated arrays

### Phase 4: Advanced
6. **Dynamic Programming**
   - [ ] Memoization vs Tabulation
   - [ ] Classic patterns (climbing stairs, knapsack)

## How to Use

Each topic folder contains:
- `README.md` - Pattern explanation with **ASCII visualizations**
- `python/` - Python solutions
- `typescript/` - TypeScript solutions

### Study Flow
1. Read the pattern README to understand the technique
2. Study the template code
3. Solve problems in Python first (usually cleaner syntax)
4. Re-implement in TypeScript for syntax practice

## Pattern Recognition Cheat Sheet

| Problem Clue | Pattern |
|--------------|---------|
| "sorted array", "find pair" | Two Pointer |
| "contiguous subarray", "window of size k" | Sliding Window |
| "range sum", "cumulative" | Prefix Sum |
| "frequency", "count occurrences" | Hash Map |
| "matching brackets", "undo" | Stack |
| "level by level", "shortest path" | BFS (Queue) |
| "all paths", "recursive structure" | DFS |
| "sorted", "minimize/maximize search" | Binary Search |
| "optimal", "count ways", "min/max" | Dynamic Programming |

## Quick Commands

```bash
# Run Python solution
python arrays-and-strings/two-pointer/python/two_sum.py

# Run TypeScript solution (with ts-node)
npx ts-node arrays-and-strings/two-pointer/typescript/two_sum.ts
```

## Progress Tracking

Track your progress by checking off problems in each README file.
