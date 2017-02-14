def passCheck():
    username=input("what is the username?")
    password=input("what is the password?")
    if username == usrcrr and password == psdcrr:
        print("you are granted access")
        
    else:
        if username == usrcrr:
            print("your password is wrong")
            passCheck();
        elif password == psdcrr:
            print("your username is wrong")
            passCheck();
        else:
            print("nothing is correct")
            passCheck();

psdcrr = "mmhmm";
usrcrr = "fellow";

passCheck();

def passCheck():
    username=input("what is the username?")
    password=input("what is the password?")
    if username == usrcrr and password == psdcrr:
        print("you are granted access")
        
    else:
        if username == usrcrr:
            print("your password is wrong")
            passCheck();
        elif password == psdcrr:
            print("your username is wrong")
            passCheck();
        else:
            print("nothing is correct")
            passCheck();

psdcrr = "mmhmm";
usrcrr = "fellow";

passCheck();

