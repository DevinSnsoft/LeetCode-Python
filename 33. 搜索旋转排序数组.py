# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
# 输入：nums = [1], target = 0
# 输出：-1

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        # 二分查找找到旋转点
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        # 确定 target 在哪个子数组中
        if target >= nums[0]:
            l, r = 0, l - 1
        else:
            l, r = l, n - 1

        # 在子数组中进行二分查找
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


nums = list(map(int, input().split()))
target = int(input())

solu = Solution()
print(solu.search(nums, target))
