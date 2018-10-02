"""
2018年9月29日20:07:33
作者:小莫先生
本模块功能: 按照数据库查询的账号ID 查询角色名及ID
"""

class AnalyticalData:
    def calc_num(self,_list_):
        """
        主要用于计算传递过来的列表重新拼合为16进制,然后再转换为10进制返回到调用程序
        """
        player_num = []
        for i in _list_:
            player_num.append(str(hex(i)).replace('0x', ''))

        return int('0x' + ''.join(player_num), 16)

    def playerData(self,player_list):
        """
        :param player_list:
        :return:
        此函数用于将传递过来的数据进行分析角色数量,以及角色ID及角色名
        """
        offset = 0
        data_head = player_list[offset:offset+2]
        offset += 2
        data_length = player_list[offset:offset+4]