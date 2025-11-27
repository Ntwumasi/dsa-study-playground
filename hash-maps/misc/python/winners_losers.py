"""
Find Players With Zero or One Losses (LeetCode 2225)

PATTERN: Hash Map - Loss Counting
- Track number of losses for each player
- Players with 0 losses never appeared as losers
- Players with 1 loss appeared as loser exactly once

TIME COMPLEXITY: O(n log n) - O(n) to process, O(n log n) to sort results
SPACE COMPLEXITY: O(n) - hash map for loss counts

WHY THIS WORKS:
- Count losses for each player using hash map
- Winners with no losses are never in the "loser" column
- We need to track all players (winners too) who have 0 losses
"""

from typing import List
from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        Find players with zero losses and players with exactly one loss.

        Args:
            matches: List of [winner, loser] pairs

        Returns:
            [players_with_0_losses, players_with_1_loss], both sorted

        Visual:
            matches = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [4,9], [10,4], [10,9]]

            Process each match, track losses:
            Player: 1  2  3  4  5  6  7  8  9  10
            Losses: 0  0  2  1  1  2  1  1  2  0

            0 losses: [1, 2, 10]
            1 loss:   [4, 5, 7, 8]

            Answer: [[1, 2, 10], [4, 5, 7, 8]]
        """
        # Track loss count for each player
        # Use -1 to indicate "seen but 0 losses" vs "never seen"
        losses = defaultdict(int)

        for winner, loser in matches:
            # Mark winner as seen (if not already marked with losses)
            if winner not in losses:
                losses[winner] = 0

            # Increment loser's loss count
            losses[loser] += 1

        # Separate players by loss count
        zero_loss = []
        one_loss = []

        for player, loss_count in losses.items():
            if loss_count == 0:
                zero_loss.append(player)
            elif loss_count == 1:
                one_loss.append(player)

        # Return sorted lists
        return [sorted(zero_loss), sorted(one_loss)]


def find_winners_sets(matches: List[List[int]]) -> List[List[int]]:
    """
    Alternative: Using three sets approach (original implementation).

    Tracks state transitions explicitly.
    """
    zero_loss = set()
    one_loss = set()
    more_losses = set()

    for winner, loser in matches:
        # Add winner to zero_loss if not already in one_loss or more_losses
        if winner not in one_loss and winner not in more_losses:
            zero_loss.add(winner)

        # Process loser - move through states
        if loser in zero_loss:
            zero_loss.remove(loser)
            one_loss.add(loser)
        elif loser in one_loss:
            one_loss.remove(loser)
            more_losses.add(loser)
        elif loser in more_losses:
            pass  # Already has 2+ losses
        else:
            # First time seeing this player (as loser)
            one_loss.add(loser)

    return [sorted(zero_loss), sorted(one_loss)]


def find_winners_counter(matches: List[List[int]]) -> List[List[int]]:
    """
    Alternative: Using Counter for cleaner syntax.
    """
    from collections import Counter

    # Count losses
    all_players = set()
    loss_count = Counter()

    for winner, loser in matches:
        all_players.add(winner)
        all_players.add(loser)
        loss_count[loser] += 1

    zero_loss = [p for p in all_players if loss_count[p] == 0]
    one_loss = [p for p in all_players if loss_count[p] == 1]

    return [sorted(zero_loss), sorted(one_loss)]


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    matches1 = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    result1 = sol.findWinners(matches1)
    print(f"Example 1: {result1}")  # [[1, 2, 10], [4, 5, 7, 8]]

    # Example 2
    matches2 = [[2, 3], [1, 3], [5, 4], [6, 4]]
    result2 = sol.findWinners(matches2)
    print(f"Example 2: {result2}")  # [[1, 2, 5, 6], []]

    # Simple example
    matches3 = [[1, 2], [2, 3]]
    result3 = sol.findWinners(matches3)
    print(f"Simple: {result3}")  # [[1], [2]]

    # Compare approaches
    print(f"\nSets approach: {find_winners_sets(matches1)}")
    print(f"Counter approach: {find_winners_counter(matches1)}")

    """
    COUNTING WITH HASH MAPS:

    This problem demonstrates several counting patterns:

    1. defaultdict(int): Auto-initializes missing keys to 0
       - losses[player] += 1 works without checking if key exists

    2. Tracking "seen but zero count":
       - Need to distinguish "0 losses" from "never played"
       - Solution: explicitly add winners with 0 losses

    3. State machine with sets:
       - Alternative approach tracking which "state" each player is in
       - More complex but shows state transition logic

    RELATED PROBLEMS:
    - Top K Frequent Elements
    - Sort Characters by Frequency
    - Group Anagrams (group by sorted string)
    - Intersection of Two Arrays
    """
