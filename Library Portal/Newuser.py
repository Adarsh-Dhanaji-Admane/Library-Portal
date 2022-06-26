#new user 

user_data = ['alex','alex@123','snel12','snel@1452']
def new_user():
    print("....you creating the New Account....\n")
    name = input("NAME :")
    phone = input("PHONE No :")
    username = input("Username :")
    password = input("Password : ")
    Confirm_Password = input("Confirm Passowrd :")
    if password == Confirm_Password:
        print(f"Hi {name}, Your Account is Created Successfully...!")
        print("kindly note that username & password..!!")
        user_data.append(username)
        user_data.append(password)
        import SignIn
        SignIn.signin(user_data)

    #elif password == Confirm_Password:
        
        

    else:
        print("\nConfirm password is not match please re-enter the proper details\n")
        print("Kindly Filled Details")
        import Home
        Home.Newuser.new_user()



           