from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ends = {}
        for i, letter in enumerate(S):
            ends[letter] = i

        partition = []
        start, end = 0, 0
        for i, letter in enumerate(S):
            end = max(end, ends[letter])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition
