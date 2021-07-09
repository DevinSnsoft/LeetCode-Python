# 求无重复字符的最长子串和长度

def getMaxLen(str):
    length = 0
    tempstr = str
    if(len(tempstr) == 0):
        length = 0
    # for i in range(1, len(tempstr)):
    #     if tempstr[i] != tempstr[0]:
    #         break
    # length = 1
    for i in range(0, len(tempstr)):
        for j in range(1, len(tempstr)):
            if tempstr[i] == tempstr[j]:
                break
    length = len(tempstr)

    return length


if __name__ == '__main__':
    str1 = ""  # 0
    str2 = "bbbb"  # b|1
    str3 = "qweigajlncmz"
    str4 = 'abcabcbb'  # abc|3
    str5 = 'pwwkew'  # wke|3,kew|3

    # print(getMaxLen(str1))
    # print(getMaxLen(str2))
    print(getMaxLen(str3))
