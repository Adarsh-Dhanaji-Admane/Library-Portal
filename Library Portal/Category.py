#subject wise section
from itertools import count
from urllib.parse import uses_relative
import SignIn

print("                 ...Welome To Publication Arts...                 ")
print("Which Subject of book you want to read??\n")

#science list
sci = ['1. Cosmos (Sagan book)','2. A Brief History of Time','3. The Origin of Species','4. The Uninhabitable Earth','5. Stephen Hawking']
choose_book = set()

print("1. Science \t 2. Technology & Programming \t 3. History \t 4. Biography \t 5. games\t 6. Exit\n")

while True:
    user_ch = input("Select anyone which you want to read :")
    if user_ch =='1' or user_ch=='science':
        print("sciences related books---->>>")
    for x in sci:
        print(x)
        
    def science(sci):
        
        while True:
            
                operations = input("\n1.Add Book \t 2. Remove Book \t3.Done \nChoose option :")
                if operations == '1':
                    print("Now Avaliable Books :",choose_book)
                    takebook = input('Add book into cart \nSelect No.:')
                    if takebook == '1':
                        choose_book.add("Cosmos (Sagan book)")
                        print(choose_book)
                    elif takebook == '2':
                        choose_book.add("A Brief History of Time")
                        print(choose_book)
                    elif takebook == '3':
                        choose_book.add("The Origin of Species")
                        print(choose_book)
                    elif takebook == '4':
                        choose_book.add("The Uninhabitable Earth")
                        print(choose_book)
                    elif takebook == '5':
                        choose_book.add("Stephen Hawking")
                        print(choose_book)
                    else:
                        print('please enter the correct number')
            
                elif operations=='2':
                    for x in sci:
                        print(x)
                    rmlist = list(choose_book)
                        #print(choose_book)
                    print("now avaliable books:",rmlist)
                    removebook = input('Remove book from cart\n Select No. :')
                    if removebook == '1':
                        rmlist.remove("Cosmos (Sagan book)")
                        print("this book is remove --> Cosmos (Sagan book)")
                        print(rmlist)
                    elif removebook == '2':
                        rmlist.remove("A Brief History of Time")
                        print("this book is remove --> A Brief History of Time")
                        print(rmlist)
                    elif removebook == '3':
                        rmlist.remove("The Origin of Species")
                        print("this book is remove -->The Origin of Species")
                        print(rmlist)
                    elif removebook == '4':
                        rmlist.remove("The Uninhabitable Earth")
                        print("this book is remove --> The Uninhabitable Earth")
                        print(rmlist)
                    elif removebook == '5':
                        rmlist.remove("Stephen Hawking")
                        print("this book is remove --> Stephen Hawking")
                        print(rmlist)
                    else:
                        print('please enter the correct number')
                
                elif operations == '3':
                    print("\nYou selected books...\n")
                    count = 0
                    #rmlist.append(choose_book)
                    
                    for j in rmlist:
                        count+=1
                        print(j)
                    print(f"Total selected books is {count}")
                    import Deatils
                    break


                else:
                    print("invalid entry") 
           


    science(sci)


        



               

            
