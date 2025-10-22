# Last updated: 10/22/2025, 12:09:25 AM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        most_repeats = max(counts)
        num_longest = counts.count(most_repeats)
        return max(len(tasks), (most_repeats-1) * (n+1) + num_longest)