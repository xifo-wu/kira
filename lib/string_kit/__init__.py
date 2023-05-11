# 判断一个字符串是否为简体中文
def is_simplified_chinese(input_str):
    for char in input_str:
        if not '\u4e00' <= char <= '\u9fa5' and not '\u9fa6' <= char <= '\u9fbb' and not '\u3400' <= char <= '\u4dbf' and not '\U00020000' <= char <= '\U0002a6df':
            return False
    return True


# 判断一个字符串是否为繁体中文
def is_traditional_chinese(input_str):
    for char in input_str:
        if not '\u2e80' <= char <= '\u2eff' and not '\u2f00' <= char <= '\u2fdf' and not '\u31c0' <= char <= '\u31ef' and not '\u3200' <= char <= '\u32ff':
            return False
    return True
