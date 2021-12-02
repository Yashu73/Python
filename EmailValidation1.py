password=input("enter password")
flag=0
while True:
        if (password)< 8:
                flag=-1
                print("password length should not less than 8 characters")
                break
        elif not re.search("[a-z]",password):
                flag=-1
                print("password must have at least one small letter")
                break
        elif not re.search("[A-Z]",password):
                flag=-1
                print("password must have at least one capital letter")
                break
        elif not re.search("[0-9]",password):
                flag=-1
                print("password must have at least one numeric")
                break
        elif not re.search("[_@$]",password):
                flag=-1
                print("password must have at least one special character")
                break
        elif not re.search("\s",password):
                flag=-1
                break
        else:
                flag=0
                print("valid password")
                break
if flag==-1:
                print("Invalid password")

