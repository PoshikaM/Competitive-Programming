class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        output = []
        for i in range(len(spells)):
            count = 0
            for j in range(len(potions)):
                temp = spells[i] * potions[j]
                if temp >= success:
                    count += 1
            output.append(count)
        return output