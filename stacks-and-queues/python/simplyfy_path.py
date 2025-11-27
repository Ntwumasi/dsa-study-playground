"""
Simplify Path (LeetCode 71)

PATTERN: Stack - Directory Navigation
- Split path by '/'
- Use stack to track current directory hierarchy
- '..' pops (go up), '.' does nothing, else push

TIME COMPLEXITY: O(n) - single pass through path
SPACE COMPLEXITY: O(n) - stack for directory names

WHY THIS WORKS:
- Stack models directory hierarchy perfectly
- Push to go into a directory
- Pop to go up to parent directory
- Build canonical path from remaining stack
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplify an absolute Unix-style file path to canonical form.

        Rules:
        - '..' means go to parent directory
        - '.' means current directory (no-op)
        - Multiple slashes treated as single slash
        - Trailing slashes removed

        Args:
            path: Absolute Unix path starting with '/'

        Returns:
            Simplified canonical path

        Visual:
            path = "/home/user/Documents/../Pictures"

            Split by '/': ['', 'home', 'user', 'Documents', '..', 'Pictures']

            Process each portion:
            - '': empty, skip
            - 'home': push -> stack = ['home']
            - 'user': push -> stack = ['home', 'user']
            - 'Documents': push -> stack = ['home', 'user', 'Documents']
            - '..': pop -> stack = ['home', 'user']
            - 'Pictures': push -> stack = ['home', 'user', 'Pictures']

            Join with '/': "/home/user/Pictures"

        Another example:
            path = "/../"
            - '': skip
            - '..': pop (but stack empty, so skip)
            - '': skip
            Result: "/"
        """
        stack = []

        # Split path by '/' and process each component
        for portion in path.split("/"):
            if portion == "..":
                # Go to parent directory (if possible)
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # Current directory or empty string - no operation
                continue
            else:
                # Valid directory name - add to path
                stack.append(portion)

        # Build canonical path
        return "/" + "/".join(stack)


def simplify_path_verbose(path: str) -> str:
    """
    Alternative: More explicit handling of edge cases.

    Same logic but with clearer comments for each case.
    """
    # Handle edge cases
    if not path:
        return "/"

    stack = []
    components = path.split("/")

    for component in components:
        # Skip empty strings (from multiple slashes or leading/trailing slash)
        if not component:
            continue

        # Skip current directory reference
        if component == ".":
            continue

        # Go up one directory
        if component == "..":
            if stack:
                stack.pop()
            # If stack is empty, we're at root - can't go higher
            continue

        # Valid directory name
        stack.append(component)

    # Build result - always starts with '/'
    if not stack:
        return "/"

    return "/" + "/".join(stack)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Simple path with parent directory
    print(sol.simplifyPath("/home/"))  # "/home"

    # Example 2: Multiple slashes and parent
    print(sol.simplifyPath("/home//foo/"))  # "/home/foo"

    # Example 3: Go above root
    print(sol.simplifyPath("/home/user/Documents/../Pictures"))
    # "/home/user/Pictures"

    # Example 4: Lots of navigation
    print(sol.simplifyPath("/../"))  # "/"

    # Example 5: Current directory
    print(sol.simplifyPath("/home/./user/./"))  # "/home/user"

    # Example 6: Complex path
    print(sol.simplifyPath("/a/./b/../../c/"))  # "/c"

    # Example 7: All special
    print(sol.simplifyPath("/./././"))  # "/"

    """
    STACK FOR PATH/HIERARCHY PROBLEMS:

    Why stack works:
    - Directories form a hierarchy (like nested structures)
    - Going into a directory = push
    - Going up (parent) = pop
    - Stack naturally tracks current "depth" in hierarchy

    Similar problems:
    1. Valid parentheses - '(' push, ')' pop and match
    2. Decode string - '[' push context, ']' pop and process
    3. Calculator - operators and operands on stack
    4. File system design - stack for current path

    PATH COMPONENTS TO HANDLE:
    - ".." -> pop (parent directory)
    - "." -> skip (current directory)
    - "" -> skip (from split on consecutive slashes)
    - name -> push (valid directory name)

    EDGE CASES:
    - Going above root: "/../../.." -> "/"
    - Multiple slashes: "//a///b" -> "/a/b"
    - Trailing slash: "/a/b/" -> "/a/b"
    - Root only: "/" -> "/"
    - Hidden files: "/.hidden" -> "/.hidden" (valid name starting with '.')
    """
