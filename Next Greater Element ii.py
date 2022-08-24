class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        Stack=[-1]*len(nums)
        monotonicStack=[]
        for i in range(len(2*nums)):
            while monotonicStack and nums[monotonicStack[-1]]<nums[i%len(nums)]:
                Stack[monotonicStack[-1]]=nums[i%len(nums)]
                monotonicStack.pop()
            if i<len(nums):
                monotonicStack.append(i)
        return Stack