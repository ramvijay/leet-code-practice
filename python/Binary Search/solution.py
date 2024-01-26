class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        leftPointer, rightPointer = 0, len(nums)-1
        while leftPointer<=rightPointer:
            midIndex = (leftPointer+rightPointer)//2
            if nums[midIndex] < target:
                leftPointer = midIndex+1
            elif nums[midIndex] > target:
                 rightPointer = midIndex-1
            else:
                return midIndex
        return -1