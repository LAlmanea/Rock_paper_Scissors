print ("____________________")
print ("Rock, Paper, Scissors, account setup")
print ("____________________")

while True:
    username = raw_input ("Pick a username:   ")
    password = raw_input ("Pick a password:   ")
    password_confirm = raw_input ("please confirm your password:   ")
    
    if password != password_confirm:
        print ("your passwords don't match, please try again.")
        
    if password == password_confirm:
        print ("your account has been set up.")
        text_file = open("accounts.txt", "a")
        text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close()
        break
        

