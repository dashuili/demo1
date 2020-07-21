"""
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入以下敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
"""

# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
# str = "000 oh yeah 0000"
# print(str.strip('0'))
"""
## note: 'a' 附加写方式不请空文件内容，'w' 会将文件内容清空然后写入，'r'读文件。

###### 写文件 ######
path = r"D:\helloworld\files\sensitive word.txt"
with open(path,'a',encoding='UTF-8') as w:
    print(w.write("comeon"))

###### 读文件 ######
# 用with语句读取\写入文本更方便简洁。
with open(path,encoding='UTF-8') as f:
    print(f.read())
"""

path = r"D:\pycharm\helloworld\files\sensitive word.txt"
def filter_word():
    with open(path, encoding='UTF-8', newline='') as f:
        content = f.read()
        return content

def main():
    words = filter_word()
    text = input('please input content: ')
    if text in words:
        print('Freedom')
    else:
        print('Human Rights')



if __name__ == '__main__':
    main()

