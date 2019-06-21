def atoz():
    ch = 'a'
    sentence = ''
    for i in range(0, 26):
        # 字符转成ascii值,例ord('a')返回97
        ascii_value = ord(ch)
        # ascii值转成字符,例chr(98)返回'b'
        char_value = chr(ascii_value + i)
        
        sentence += char_value
    return sentence


print(atoz())
