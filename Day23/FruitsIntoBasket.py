class Solution(object):
    def totalFruit(self, fruits):
        if not fruits:
            return 0

        maxcount = 0
        fruitcount = {}
        left = 0

        for i in range(len(fruits)):
            fruitcount[fruits[i]] = fruitcount.get(fruits[i], 0) + 1

            while len(fruitcount) > 2:
                fruitcount[fruits[left]] -= 1
                if fruitcount[fruits[left]] == 0:
                    del fruitcount[fruits[left]]
                left += 1

            maxcount = max(maxcount, i - left + 1)

        return maxcount