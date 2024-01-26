class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        totalBananas = 0
        for pile in piles:
            totalBananas += pile
        lowestK =  math.ceil(totalBananas/h)
        maxK = max(piles) 
        k = maxK
        while lowestK <= maxK:
            midK = (maxK + lowestK) // 2
            hours = 0
            for pile in piles:
                hours = hours + math.ceil(pile/midK)
            print (hours, midK)
            if hours <= h:
                k = min(k, midK)
                maxK = midK - 1               
            else:                 
                lowestK = midK  + 1                           
        return k
                