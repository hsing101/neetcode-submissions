class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = defaultdict(int)
        for num in hand:
            count[num] += 1
        hand.sort()
        i = 0
        while i < len(hand):
            start = hand[i]
            while count[start] > 0:
                for j in range(groupSize):
                    if count[start + j] == 0:
                        return False
                    count[start + j] -= 1
            i += 1
        return True

