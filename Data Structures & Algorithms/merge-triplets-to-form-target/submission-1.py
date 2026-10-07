class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i in range(len(target)):
            found = False
            for triplet in triplets:
                if triplet[i] != target[i]:
                    continue
                if (triplet[0] <= target[0] and
                    triplet[1] <= target[1] and
                    triplet[2] <= target[2]):
                    found = True
                    break

            if not found:
                return False

        return True
                
                
                
                

        