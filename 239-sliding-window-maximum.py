from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        i = 0
        j = 0
        ans = []
        while j < len(nums):
            while dq and nums[j] > dq[-1]: dq.pop()
            dq.append(nums[j])
            if j-i+1 < k:
                j += 1
            else:
                ans.append(dq[0])
                if nums[i] == dq[0]:dq.popleft()
                i += 1
                j += 1
        print(ans)
        return ans
