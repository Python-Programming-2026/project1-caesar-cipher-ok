#凯撒密码：加密函数
def encrypt(text,shift): #传送两个参数：需要加密的文本和位移量
    result = "" #定义一个空的字符串，用来储存结果
    for char in text: #对文本的每个字符进行转换
        if(char.isalpha()): #判断字符是否是字母
            if(char.isupper()):start = ord('A') #判断字符是大写还是小写
            else: start = ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        #让字符的ASCII码值减去A或a的ASCII值，再加上位移量，超过26的取余，再加上A或a的ASCII值，即完成了转换
        else:
            result += char #数字不进行转换
    return result

def decrypt(text,shift):#凯撒密码：解密函数
    return encrypt(text,-shift) #用位移量的相反数进行加密即为解密

# 交互式主程序
if __name__ == "__main__":
    print("=== 凯撒密码工具 ===")
    # 让用户选择模式
    mode = input("请选择模式（encrypt 加密 / decrypt 解密）：")
    # 让用户输入文本
    text = input("请输入要处理的文本：")
    # 让用户输入偏移量（转成整数）
    shift = int(input("请输入偏移量（数字）："))

    # 根据模式执行对应操作
    if mode == "encrypt":
        result = encrypt(text, shift)
        print(f"加密结果：{result}")
    elif mode == "decrypt":
        result = decrypt(text, shift)
        print(f"解密结果：{result}")
    else:
        print("模式输入错误，请输入 encrypt 或 decrypt")