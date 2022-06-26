#previous user and new user data
import Newuser


def signin(user_data):
    print("       ...Sign In...         \n")
    username = input("USERNAME :")
    password = input("PASSWORD :")
    
    if username and password in user_data:
        print("\nSuccessfully Login...")
        
        import Category

    else:
        print("Invalid Username & Password")
        print("Kindly Filled Details")

