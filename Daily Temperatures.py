#Time Complexity: O(n);
#Space Complexity: O(n);

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures);
        output=[0]*n;
        stack=[];
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                output[stack[-1]]=i-stack[-1];
                stack.pop();
            stack.append(i);
        return output;