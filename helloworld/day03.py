
# split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串 。split('')以空格为空格符。
path = r"D:\pycharm\helloworld\files\word"
"""
list = []
with open(path, encoding='UTF-8') as f:
    for content in f:
        list.append(content.strip())

    print(list)
"""
# 任一个英文的纯文本文件，统计其中的单词出现的个数。

import collections

with open(path,'r') as f:
    content=f.read().split(' ')# split (' ')将文件中的内容以空格分隔出来，然后存入列表
    print(content)
b = collections.Counter(content) #Counter以字典的键值对形式存储并计数，其中元素作为key，其计数作为value。
print(b)
print(b.items())
with open('files/result2.txt', 'w') as result_file: # 直接打开一个文件，如果文件不存在则创建文件
    for key,value in b.items(): #  b.items() 返回可遍历的(键, 值) 元组数组。
        result_file.write(key+':'+str(value)+'\n') # python中数字不能像Java一样自动转换为字符串进行拼接，需要借助str()函数进行转化将数字转换成字符串类型
file = open("files/result2.txt", 'r') # w 只能写不能读，要想输出到控制台必须先读 ‘r’ ，在print
print(file.read())


