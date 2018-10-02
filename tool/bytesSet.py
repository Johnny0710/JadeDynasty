def ziJieJi(Integer):


    # 将传递过来的整数型转换为十六进制,切片取出需要的数据
    hexx = hex(Integer)[2:]
    # 获取转换后的十六进制长度
    lenth = len(hexx)

    # 创建两个空列表用于接收新数据
    new_li = []
    int_li = []

    # 判断长度,如果16进制长度小于10则补位,Python中的十六进制表示:0xffffff
    if lenth < 8:
        for i in range(8 - lenth):
            hexx = '0'+ hexx
    # 使用for循环切片取出需要的部分,加入到新的列表中
    for i in range(0, 8, 2):
        int_li.append(int(hexx[i:i + 2], 16))
    return  int_li


if __name__ == '__main__':
    print(ziJieJi(528))