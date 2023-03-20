class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def binary_search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        left_index = binary_search_left(nums, target)
        right_index = binary_search_right(nums, target)

        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    sol = Solution()
    ans = sol.searchRange(nums, target)
    print(ans)
