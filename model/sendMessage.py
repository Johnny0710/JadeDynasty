from tool.bytesSet import ziJieJi
from tool.pwUnicode import pwtrans
player_num = [141, 73, 8, 128, 0, 0, 0]

def playerNum(AccountID):

    player_num.extend(ziJieJi(AccountID))

    return player_num

def sendRadio(string):
    radio_head = [128, 79]
    radio_link = [9, 73, 0, 0, 4, 0, 0, 0, 0, 18]
    radio_body = pwtrans(string)
    radio_body_len = [len(radio_body)]

    radio_end = [0]

    radio_link.extend(radio_body_len)
    radio_link.extend(radio_body)
    radio_link.extend(radio_end)
    radio_all_len = len(radio_link)

    if radio_all_len <128:
        radio_head.extend([radio_all_len])
    else:
        radio_head.extend([128,radio_all_len])

    radio_head.extend(radio_link)
    radio_head.extend(radio_end)

    return  bytes(radio_head)

def sendMial(player_id=None,mail_title="恭喜您获得奖品",mail_body="这是GM发送给您的奖品，请注意查收附件！",items_id=0,items_num=0):
    mail_head = [144,118]  # 一
    mail_link = [128,0,0,6,0,0,4,0,3] # 三
    player_id_tr = ziJieJi(player_id)
    mail_title_tr = pwtrans(mail_title) # 五
    mail_body_tr = pwtrans(mail_body) # 七
    items_id_tr = ziJieJi(items_id)# 八  物品ID
    unknown = [0,0,0,0]  # 九
    items_num_tr = ziJieJi(items_num)  # 十  & 十一
    mail_end = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  # 十二
    title_length = len(mail_title_tr) # 四
    body_length = len(mail_body_tr)  # 六

    mail_link.extend(player_id_tr)
    mail_link.extend([title_length])
    mail_link.extend(mail_title_tr)
    mail_link.extend([body_length])
    mail_link.extend(mail_body_tr)
    mail_link.extend(items_id_tr)
    mail_link.extend(unknown)
    mail_link.extend(items_num_tr)
    mail_link.extend(items_num_tr)
    mail_link.extend(mail_end)

    mail_all_length = len(mail_link)
    if mail_all_length < 128:
        mail_all_length = [len(mail_link)]
    else:
        mail_all_length = [128,len(mail_link)]

    mail_head.extend(mail_all_length)
    mail_head.extend(mail_link)
    return bytes(mail_head)

def sendCloseGame(second):
    mesage = [129, 102, 16, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0]
    mesage.extend(ziJieJi(second))
    return bytes(mesage)


