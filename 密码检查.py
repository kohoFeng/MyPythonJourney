# 任务：编写函数检查密码是否符合以下条件：
# - 长度≥8
# - 包含至少1个大写字母、1个小写字母和1个数字
# - 至少包含以下特殊符号：!@#$%
import re
def check_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d',password):
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'[!@#$%]',password):
        return False
    return True


print(check_password("Abc123#"))   # 应返回False（长度不足）
print(check_password("Abcdef123")) # 应返回False（缺少特殊符号）
print(check_password("Abc!1234"))  # 应返回True

# 当一个字符串以r前缀开始时，它将被视为原始字符串，其中的转义字符将被忽略。