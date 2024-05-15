    #email vaildation using string function
email=input("enter vaild email: ")
k,d,j=0,0,0
if len(email)>=12:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if(email[-4]==".")^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or d==1 or j==1:
                    print("somthing want to wrong")
                else:
                    print("right email address")
            else:
                print("pleace check '.' ")
        else:
            print("In email we have only one '@'")
    else:
        print("email first character should be alphabate")
else:
    print("your email lenght is not vaild")
    