# 任务：将输入的10位数字转换为"(123) 456-7890"格式
# 若输入非10位纯数字，返回"Invalid input"
import re
def format_phone(num_str):
    if re.search(r'\d{10}',num_str) and len(num_str) == 10:
        result = f"({num_str[:3]}){num_str[3:6]}-{num_str[6:]}"
        return result
    else:
        result = "Invalid input"
        return result

print(format_phone("1234567890"))  # 应返回 "(123) 456-7890"
print(format_phone("12a45b7890"))  # 应返回 "Invalid input"
