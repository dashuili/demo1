array1 =  {
        "username": "pyuser1@exhr-14201dom.extest.microsoft.com",
        "receive_address": "user1@exhr-14201dom.extest.microsoft.com",
        "cc_address": "test1@exhr-14201dom.extest.microsoft.com",
        "subject": "111",
        "password": "T%nt0wn",
        "receive_password": "T%nt0wn",
        "cc_password": "T%nt0wn",
        "action": "format",
        "switch": "replyall",

        "body1": "this is first message",
        "body2": "test reply"
    }
print(array1.keys())
print(array1.values())
for item in array1:
    if item == "body1":
        print(array1["body1"])