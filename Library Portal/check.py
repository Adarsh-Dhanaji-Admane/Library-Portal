#import Newuser
dict = ['alex','alex123', 'b','also','c','alex123@','alex123']

def signins():

    print(dict)  
    key = input("enter 1:")
    value = input("enter:")
    while True:
        if key and value in dict:
            #d31print("present",Newuser.New_user())
            break
        else:
            print("Invalid entry")
            break
        
def new():
    print("new user")
    user = input("username:")
    passd = input("password:")
    dict.append(user)
    dict.append(passd)
    print(dict)
    signins()


new()