class Solution:
    def binarySearch(self, startIndex: int, endIndex: int, numbers: List[int], target: int):
        
        if(startIndex == endIndex):
            if numbers[startIndex] == target:
                return startIndex
            else:
                return -1

        mid = startIndex + (endIndex-startIndex)//2
        print(mid)
        if target == numbers[mid]:
            return mid
        elif target < numbers[mid]:
            return self.binarySearch(startIndex,mid-1,numbers,target)
        else:
            return self.binarySearch(mid+1,endIndex,numbers,target)
        
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            number = numbers[i]
            if self.binarySearch(i, len(numbers)-1, numbers, target-numbers[i]) != -1 :
                return [i+1, self.binarySearch(i,len(numbers)-1, numbers, target-numbers[i])+1]