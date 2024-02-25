first =input("Enter Your First Name :").upper()
if all(x.isalpha() for x in first):
    print("First Name is Full of Letters ",first)
    last = input("Enter Your Last Name :").upper()
    if all(x.isalpha() for x in last):
        print("Last Name is Full of Letters ",last)
        age = int(input("Enter Your Age :"))
        if age < 0:
            print("Invalid Age Input")
        else:
            print("Age :" , age)
            contact = input("Enter Your Contact Number :")
            if len(contact)==10 or not contact.isdigit():
                print("Contact Number :",contact)
            
                gmail = input("Enter Your Gmail id :")
                if gmail[-10:]== "@gmail.com":
                    
                 print(" G-mail ID  :", gmail)
                else:
                    print("invalid Gmail")
            else:
                print("Invalid Contact num")
    else:
        print("Invalid Last Name ")
else:
    print("Invalid first Name")
                        
    
       
