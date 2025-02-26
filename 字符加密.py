# 任务：实现凯撒密码加密（字母后移3位，z→c，保留大小写和非字母字符）
def caesar_encrypt(text):
    result = []
    for char in text:
        if char.isalpha():
            boundary = 65 if char.isupper() else 97
            shifted = (ord(char) - boundary + 3) % 26 + boundary
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

print(caesar_encrypt("Hello, World!"))  # 应返回 "Khoor, Zruog!"

#ord():以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值