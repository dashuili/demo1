from selenium import webdriver
#driver = webdriver.Chrome()
#driver.implicitly_wait(10)
#driver.maximize_window()

#driver.get("https://10.194.249.152/owa")

"""
phrase = "giraffe acvemay"
list=[]
print(len(phrase))
print(phrase[2])
#hobby=input("")
#print("hello" + hobby)

# list, we can put stings, numbers, or booleans, etc
friend = ["kevin", "karen", "jim"]
print(friend[2])
# 只取索引位1往后的部分包括1
print(friend[1:])

#基本函数
def say_hi(name,age):
    print("hello" + name+"your age:"+ str(age))

say_hi("mike",24)


def cube(num):
    print("hi")
    return num*num*num
    print("it won't be executed") #return语句后面的将不会执行

cube(2) # 不会显示return的值，只有print函数将其打印出来才会显示
print(cube(3))


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99) #
bart = Student('Bart', 59)
print(lisa.name,lisa.score, lisa.grade())
print(bart.name,bart.score, bart.grade())
"""
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa', 99)
bart.print_score()
print(bart.name, bart.get_grade())
print(lisa.name,lisa.get_grade())

scores = {'数学': 95, '语文': 89, '英语': 90}
print(scores['英语'])
print(scores.keys())
print(scores.values())
print(scores.items())

a = {'数学': 95, '语文': 89, '英语': 90}
b = list(a.keys())
print(b)

a = {'数学': 95, '语文': 89, '英语': 90}
for k in a.keys():
    print(k,end=' ')
print("\n---------------")
for v in a.values():
    print(v,end=' ')
print("\n---------------")
for k,v in a.items():
    print("key:",k," value:",v)