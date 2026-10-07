class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = defaultdict(int)
        for num in hand:
            count[num] += 1
        hand.sort()
      
        for num in hand:
            if count[num] == 0:
                continue

            for card in range(num, num + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1
        return True