import sys, time, os

def Scroll_Print(message, value, newline = False, speed = 0.03):
    if newline == True:
        print("\n")
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    if value == "True":
        return input(":")
websites = []
usernames = []
passwords = []

while True:
    newWebsite = input("Would you like to enter another website? Y/N")
    
    if newWebsite.upper()[0] == "Y":
        while True:
            if newWebsite.upper()[0] == "Y":
                websites.append(Scroll_Print("Please enter the website name", "True").lower())        
                usernames.append(Scroll_Print("What would you like this website's username to be", "True").lower())   
                passwords.append(Scroll_Print("What would you like this website'password to be", "True").lower()) 
                response = Scroll_Print("Would you like to enter another website? Y/N", "True").upper()

                if response == "N":
                    break
    
    while True:
        how_Many_Passwords = Scroll_Print("Would you like to print one or all passwords? 1/all", "True", True)

        if how_Many_Passwords == "1":
            requested_Web = Scroll_Print("What is the name of the website you want to obtain your information for?", "True")
            if requested_Web.lower() in websites:
                index = websites.index(requested_Web)
                Scroll_Print("Website:" + websites[index] + "    Username:" + usernames[index] + "    Password:" + passwords[index], False, True)
                break
            else:
                print("You have no website", requested_Web)
        elif how_Many_Passwords.upper() == "ALL":
            for index in range (len(websites)):
                joined = "".join("Website:" + websites[index] + "     Username:" + usernames[index] + "    Password:" + passwords[index])
                Scroll_Print(joined, False, True, 0.02)
            break
        break
    print("\n")
