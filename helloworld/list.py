"""
data=range(0,5)
result= []
for i in data:
    if i>2:
        result.append(i)
print(result)

"""

path = r"D:\pycharm\helloworld\files\sensitive word.txt"
def filtered_words(path):
    words = []
    with open(path, 'r', encoding='utf-8', newline='') as f:
        for line in f:
            words.append(line.strip())
    print(words)
    return words

def main():
    words = filtered_words(path)
    while True: # 死循环
        text = input('content: ').strip()
        if text in words:
            print('Freedom')
        else:
            print('Human Rights')
main()