import codecs

def pwtrans(string):
    lll = []
    length = 0
    for i in string:
        uni = codecs.unicode_escape_encode(i)[0]
        string = str(uni)
        if string.find(r"b'\\") == 0:
            string = string.replace(r"b'\\u", '')
            string = string.replace(r"'", '')
            lll.append(int('0x' + string[2:], 16))
            lll.append(int('0x' + string[0:2], 16))
            length += 2

        else:
            string = string.replace(r"b'",'')
            string = string.replace(r"'", '')
            lll.extend([ord(string),0])
            length += 0

    return bytes(lll)