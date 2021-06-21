# 整数数组nums
# 整数目标值target
# 在数组中找出和为target的两个整数，并返回数组下标

import datetime


def findTarget(numbers, target):
    for i in range(0, len(numbers)):
        if target - numbers[i] in numbers:
            return numbers[i], i, target - numbers[i]


def findValueSub(numbers, value):
    for j in range(0, len(numbers)):
        if value == numbers[j]:
            return j


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    startTime = datetime.datetime.now()
    num, num2, num3 = findTarget(nums, 33)
    num4 = findValueSub(nums, num3)
    endTime = datetime.datetime.now()
    print(num, num3, num2, num4)
    print("时间复杂度为：", endTime - startTime)
