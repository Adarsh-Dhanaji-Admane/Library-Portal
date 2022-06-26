import imp
from Newuser import new_user

def userdetails():
    print("\nHello")
    print("In which format you want this books like online or Offline\n") 
    while True:
        ans = input('Enter you answer (1. online or 2. offline) :')
        if ans == '1':
            print("Enter the email address for soft copy\n")
            email = input("Email :")
            print("thank you")
            con = input("hey , You want to 1.continue or 2.exit :")
            if con =='1':
                import Home
            else:
                print("\nThank To Visiting Us..bye take care")
                break


        elif ans == '2':
            print("...please filled this details...")
            name = input("NAME :")
            Add = input("ADDRESS :")
            Phoneno = input("PHONE NO :")
            username = input("USERNAME :")
            print("\nYour Deatils is Submitted \n")
            print("your Booking ID is ",id(username))
            print()
            con = input(f"hey {name}, You want to 1.continue or 2.exit :")
            if con =='1':
                import Home
            else:
                print("\nThank To Visiting Us..bye take care")
                break

        else:
            print('invalid entry')
userdetails()


