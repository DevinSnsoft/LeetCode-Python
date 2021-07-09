# 两个非空链表，表示两个非负的整数
# 逆序存储，每个节点存储一位数字
# 两个数相加，以相同形式返回一个和的链表


def addTwo(l1, l2):
    if len(l1) >= len(l2):
        l3 = [0 for i in range(len(l1)+1)]
    else:
        l3 = [0 for i in range(len(l2)+1)]

    temp = 0
    if len(l2) <= len(l1):
        for j in range(0, len(l2)):
            if (l1[j] + l2[j]) >= 10:
                l3[j] = (l1[j] + l2[j]) - 10 + temp
                temp = 1
            else:
                l3[j] = l1[j] + l2[j] + temp
                temp = 0
        for j in range(len(l2), len(l1)):
            if (l1[j] + temp) >= 10:
                l3[j] = l1[j] + temp - 10
                temp = 1
            else:
                l3[j] = l1[j] + temp
                temp = 0
        l3[len(l3)-1] = l3[len(l3)-1] + temp
        if l3[len(l3)-1] == 0:
            l3.pop()
        return l3
    else:
        for j in range(0, len(l1)):
            if (l1[j] + l2[j]) >= 10:
                l3[j] = (l1[j] + l2[j]) - 10 + temp
                temp = 1
            else:
                l3[j] = l1[j] + l2[j] + temp
                temp = 0
        for j in range(len(l1), len(l2)):
            if (l2[j] + temp) >= 10:
                l3[j] = l2[j] + temp - 10
                temp = 1
            else:
                l3[j] = l2[j] + temp
                temp = 0
        l3[len(l3) - 1] = l3[len(l3) - 1] + temp
        if l3[len(l3) - 1] == 0:
            l3.pop()
        return l3


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [2, 3, 4]
    list3 = [9, 9, 9, 9, 9, 9, 9]
    list4 = [8, 8, 8, 8]
    result1 = addTwo(list2, list1)
    result2 = addTwo(list3, list4)
    print(result1)
    print(result2)
