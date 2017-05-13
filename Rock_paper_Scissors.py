#Made by Latifah Almanea
import time
lose = ("The computer wins")
win = ("You win")
lives = 5
score = 0
drew = 0
computer_lives = 7
password_list = []
while True:
    print ("To begin fill in the below information")
    username = raw_input("Please enter your username:  ")
    password = raw_input("Please enter you password:   ")
    searchfile = open("accounts.txt","r")
    for line in searchfile:
        password_list.append(line.strip())
        if username and password in password_list:
            print ("access granted")
            time.sleep(0.5)
            print("Loading.")
            time.sleep(0.5)
            print("Loading..")
            time.sleep(0.5)
            print("Loading...")
            time.sleep(0.5)
            print ("_________________________________________________________")
            print ("rock paper scissors (please only enter your choice in lower case letter)")
            print ("_________________________________________________________")
            print ("Live Rules")
            print ("You start with", lives, "lives")
            print ("If you win you get an extra live.")
            print ("If you lose, you lose a live.")
            print ("---------------------------------")
            
            while True:
                rps = raw_input("rock, paper, scissors?   ")
                import random
                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)
                #rock if statments
                if rps == "rock" and computer == "paper":
                    print ("The computer choose", computer)
                    print ("")
                    print (lose)
                    print ("")
                    print ("")
                    lives -= 1
                    
                if rps == "rock" and computer == "scissors":
                    print ("The computer chooses", computer)
                    print ("")
                    print (win)
                    print ("")
                    print ("")
                    score += 1
                    
                #paper if statments
                if rps == "paper" and computer == "rock":
                    print ("The computer choses", computer)
                    print ("")
                    print (win)
                    computer_lives -= 1
                    print ("")
                    print ("")
                    score += 1
                    
                if rps == ("paper") and computer == "scissors":
                    print ("The computer choses", computer)
                    print ("")
                    print (lose)
                    print ("")
                    print ("")
                    lives -= 1
                    
                #scissors if statments
                if rps == "scissors" and computer == "rock":
                    print ("The computer choses", computer)
                    print ("")
                    print (win)
                    computer_lives -= 1
                    print ("")
                    print ("")
                    lives += 1
                    
                if rps == "scissors" and computer == "rock":
                    print ("The computer choses", computer)
                    print ("")
                    print (lose)
                    print ("")
                    print ("")
                    lives -= 1
                    
                #duplicates
                if rps == "rock" and computer == "rock":
                    print ("The computer choses", computer)
                    print ("")
                    print ("You drew")
                    print ("")
                    print ("")
                    drew += 1
                    
                if rps == "paper" and computer == "paper":
                    print ("The computer choses", computer)
                    print ("")
                    print ("You drew")
                    print ("")
                    print ("")
                    drew += 1
                    
                if rps == "scissors" and computer == "scissors":
                    print ("The computer choses", computer)
                    print ("")
                    print ("You drew")
                    print ("")
                    print ("")
                    drew += 1
                    
                #systems
                if rps == "rules":
                    print ("*************************")
                    print ("Rules")
                    print ("*************************")
                    print ("-rock loses against paper")
                    print ("-rock beats scissors")
                    print ("-paper beats rock")
                    print ("-Papaer loses against scissors")
                    print ("-scissors beats paper")
                    print ("-scissors loses against rock")
                    print ("**************************")
                    
                if rps == "display lives":
                    print (lives)
                    
                if rps == "display score":
                    print (score)
                    
                if rps == "display drew":
                    print (drew)
                    
                #lives
                if lives == 0 or rps == "test":
                    print ("Thanks for playing")
                    print ("You have ran out of lives")
                    print ("You got", score, "correct")
                    print ("You drew", drew, "times")
                    stop = raw_input ("press enter to exit")
                    import time
                    time.sleep(900)
                if computer_lives == 0:
                    print ("Thanks for playing")
                    print ("The computer lost all its lives. You win")
                    print ("You got", score, "correct")
                    print ("You drew", drew, "times")
                    stop = raw_input ("press enter to exit")
                    import time
                    time.sleep(900)
                    
                #exit
                if rps == "exit":
                    break
                    
        else:
            print ("You username or password is incorrect.")
            print ("______________________________________")
