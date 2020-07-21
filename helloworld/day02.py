
d = {'name':'maaz','password':'T%nt0wn'}
print(d['name'])
print(d.keys())
print(d.values())
while True: #进入循环
    name = input("请输入您的用户名：")
    if name in d.values():
        break
    else:
        print("用户不存在")

while True:
    pwd = input("输入你到密码")
    if d['password'] == pwd:
        print("进入系统")
        break
    else:
        print("密码不匹配")


