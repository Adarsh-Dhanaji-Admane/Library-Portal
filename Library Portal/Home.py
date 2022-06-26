
greeting = ("         <<--------------__Publication Arts__-------------->>            \n")
print(greeting)
print(" Welcome To Publication Arts is Public Library if you want to read book then you can read online and offline on your place.")
#Menu
#print("\n           Home \t 2. New User \t 3. Sign In \t 4.Exit           \n")
#choose = input("Kindly enter the Choice  :")
#home page operation
user_date = ['alex','alex@123','snel12','snel@1452']
while True:
    print("\n           Home \t 2. New User \t 3. Sign In \t 4.Exit           \n")
    choose = input("Choose Menu:")
    
    if choose =='2' or choose == 'new user':
        print(f"Hello Dear, you choose the {choose} --> create new aacount.")
        import Newuser
        Newuser.new_user()
    elif choose =='3' or choose == 'sign in':
        print(f"Hello Dear, you choose the {choose} --> Sign in Account.")
        import SignIn
        SignIn.signin(user_date)
        
    elif choose=='4' or choose =='close':
        print(f"Hello Dear, you choose the {choose} --> Exit in NMMC public library.")
        print("Thank You For Visiting Us Bye...!!")
        break 
    else:
        print("Invalid Enter the entry!")
        print("please enter the correct one...")
        pass     







