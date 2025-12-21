
#Link to data:https://docs.google.com/spreadsheets/d/1Ho9lPCciQyw3vW9ETZInckz9vHTDXCol2Hg-ODz8x84/edit?usp=sharing

import sys
bankinfo = None
wincondition = "no"

print("What is your name?")
name = input()
if name == "Li'el":
    print("Why are you playing your own game???")
    sys.exit()
    

print("Hello " + str(name) + "!")
print("Welcome to an NFL team guesser!(For teams with more than 1 superbowl wins!)")


print("How many superbowl wins has your team gotten?")
sprbwlwins = input()

while sprbwlwins not in ("0","1","2","3","4","5","6"):#Makes sure that the value of wins is from a range of 0 to 6
    print("Please input how many superbowl wins your team has gotten from a range of 0 to a range of 6: ")
    sprbwlwins = input()


if int(sprbwlwins) > 1 and int(sprbwlwins) < 7:#Checks if the superbowl wins is in the range of 2 - 6
    print("Your team did better than half of the league!")
    print("What conference does your team play in? The AFC or NFC?")
    conference = input()

    while conference.lower().strip() != "nfc" and conference.lower().strip() != "afc":# When the answer isn't either, it loops
        print("What conference is your team in?")
        conference = input()
        
    
    if conference.strip().lower() == "nfc":  #Asks if the team has an animal mascot
        print("Does your team have an animal mascot?")
        animascot = input()

        while animascot.lower().strip() != "yes" and animascot.lower().strip() != "no":# When the answer isn't either, it loops
            print("Please respond yes or no!")
            animascot = input()

        if animascot.lower().strip() == "yes":
            print("Was your team established before 1960?")#Branching if statement to determine establishment
            date = input()

            while date.strip().lower() != "yes" and date.strip().lower() != "no":# When the answer isn't either, it loops
                print("Please respond YES or NO!")
                date = input()

            if date.lower().strip() == "yes":#Asks if it was a winning season
                print("Did your team have a winning season in 2024?")
                winseason = input()

                while winseason.lower().strip() != "yes" and winseason.lower().strip() != "no":#Loops if not acceptable
                    print("ANSWER THE QUESTION!!!")
                    winseason = input()

                if winseason.lower().strip() == "yes":
                        print("Do they play in one of the original 13 colonies?")#Asks the team
                        colonyyesorno = input()

                        while colonyyesorno.lower().strip() != "yes" and colonyyesorno.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            colonyyesorno = input()
    
                        if colonyyesorno.lower().strip() == "no":
                            print("Is your team the Los Angeles Rams?")#Asks the team
                            wincondition = input()
                            
                            while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                                print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                                wincondition = input()
                                
                        elif colonyyesorno.lower().strip() == "yes":
                            print("Is your team the Philadelphia Eagles?")#Asks the team
                            wincondition = input()

                            while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                                print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                                wincondition = input()
    

            elif date.lower().strip() == "no":
                print("Did your team have a winning season in 2024?")
                winseason = input()

                while winseason.lower().strip() != "yes" and winseason.lower().strip() != "no":#Loops if not acceptable
                    print("ANSWER THE QUESTION!!!")
                    winseason = input()

                wincondition = "no"#Ends the game because it is not possible

                

                
                

                

        elif animascot.lower().strip() == "no":
            print("Was your team established before 1960?")#Branching if statement to determine establishment
            date = input()

            while date.strip().lower() != "yes" and date.strip().lower() != "no":# When the answer isn't either, it loops
                print("Please respond YES or NO!")
                date = input()

            if date.lower().strip() == "yes":
                print("Did your team have a winning season in 2024?")#Asks if they won the season
                winseason = input()

                while winseason.lower().strip() != "yes" and winseason.lower().strip() != "no":#Loops if not acceptable
                    print("ANSWER THE QUESTION!!!")
                    winseason = input()

                if winseason.lower().strip() == "yes":
                        print("Do they play in one of the original 13 colonies?")#Asks the team
                        colonyyesorno = input()

                        while colonyyesorno.lower().strip() != "yes" and colonyyesorno.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            colonyyesorno = input()
    
                        if colonyyesorno.lower().strip() == "no":
                            print("Is your team the Green Bay Packers?")#Asks the team
                            wincondition = input()
                            
                            while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                                print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                                wincondition = input()
                                
                        elif colonyyesorno.lower().strip() == "yes":
                            print("Is your team the Washington Commanders?")#Asks the team
                            wincondition = input()

                            while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                                    print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                                    wincondition = input()

                elif winseason.lower().strip() == "no":
                        print("Do they play in one of the original 13 colonies?")#Asks the team
                        colonyyesorno = input()
                        

                        while colonyyesorno.lower().strip() != "yes" and colonyyesorno.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            colonyyesorno = input()
    
                        if colonyyesorno.lower().strip() == "yes":
                            print("Is your team the New York Giants?")#Asks the team
                            wincondition = input()
                            
                            while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                                print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                                wincondition = input()
                                
                        elif colonyyesorno.lower().strip() == "no":
                            print("Is your team the San Francisco 49ers?")#Asks the team
                            wincondition = input()

                            while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                                    print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                                    wincondition = input()

            elif date.lower().strip() == "no":
                print("Did your team have a winning season in 2024?")
                winseason = input()

                while winseason.lower().strip() != "yes" and winseason.lower().strip() != "no":#Loops if not acceptable
                    print("ANSWER THE QUESTION!!!")
                    winseason = input()

                if winseason.lower().strip() == "yes":
                        print("Is the team you are thinking about the Tampa Bay Buccaneers?")#Asks the team
                        wincondition = input()
                            
                        while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            wincondition = input()


                elif winseason.lower().strip() == "no":
                        print("Is the team you are thinking about the Dallas Cowboys?")#Asks the team
                        wincondition = input()
                            
                        while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            wincondition = input()

                

            
    elif conference.strip().lower() == "afc":  #Asks if the team has an animal mascot
        print("Does your team have an animal mascot?")
        animascot = input()

        while animascot.lower().strip() != "yes" and animascot.lower().strip() != "no":# When the answer isn't either, it loops
            print("Please respond yes or no!")
            animascot = input()

        if animascot.lower().strip() == "yes":
            print("Was your team established before 1960?")#Branching if statement to determine establishment
            date = input()

            while date.strip().lower() != "yes" and date.strip().lower() != "no":# When the answer isn't either, it loops
                print("Please respond YES or NO!")
                date = input()

            if date.lower().strip() == "yes":
                print("Did your team have a winning season in 2024?")
                winseason = input()

                while winseason.lower().strip() != "yes" and winseason.lower().strip() != "no":#Loops if not acceptable
                    print("ANSWER THE QUESTION!!!")
                    winseason = input()

                if winseason.lower().strip() == "yes":
                    wincondition = "no"

                    while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            wincondition = input()
                            
                elif winseason.lower().strip() == "no":
                        print("Is the team you are thinking about the Indianapolis Colts?")#Asks the team
                        wincondition = input()
                            
                        while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            wincondition = input()

            elif date.lower().strip() == "no":
                print("Did your team have a winning season in 2024?")
                winseason = input()

                while winseason.lower().strip() != "yes" and winseason.lower().strip() != "no":#Loops if not acceptable
                    print("ANSWER THE QUESTION!!!")
                    winseason = input()
                

                if winseason.lower().strip() == "yes":
                        print("Do they play in one of the original 13 colonies?")#Asks the team
                        colonyyesorno = input()
                        

                        while colonyyesorno.lower().strip() != "yes" and colonyyesorno.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            colonyyesorno = input()
    
                        if colonyyesorno.lower().strip() == "yes":
                            print("Is your team the Baltimore Ravens?")#Asks the team
                            wincondition = input()
                            
                            while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                                print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                                wincondition = input()
                                
                        elif colonyyesorno.lower().strip() == "no":
                            print("Is your team the Denver Broncos?")#Asks the team
                            wincondition = input()

                            while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                                    print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                                    wincondition = input()

                
                
                elif winseason.lower().strip() == "no":
                        print("Is your team the Miami Dolphins?")#Asks the team
                        wincondition = input()
                            
                        while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            wincondition = input()

                                
        elif animascot.lower().strip() == "no":
            print("Was your team established before 1960?")#Branching if statement to determine establishment
            date = input()

            while date.strip().lower() != "yes" and date.strip().lower() != "no":# When the answer isn't either, it loops
                print("Please respond YES or NO!")
                date = input()

            if date.lower().strip() == "yes":
                print("Did your team have a winning season in 2024?")#Asks if they had a winning season
                winseason = input()

                while winseason.lower().strip() != "yes" and winseason.lower().strip() != "no":#Loops if not acceptable
                    print("ANSWER THE QUESTION!!!")
                    winseason = input()

                if winseason.lower().strip() == "yes":
                        print("Is the team you are thinking about the Pittsburgh Steelers?")#Asks the team
                        wincondition = input()
                            
                        while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            wincondition = input()

            elif date.lower().strip() == "no":
                print("Did your team have a winning season in 2024?")
                winseason = input()

                while winseason.lower().strip() != "yes" and winseason.lower().strip() != "no":#Loops if not acceptable
                    print("ANSWER THE QUESTION!!!")
                    winseason = input()


                if winseason.lower().strip() == "yes":
                    print("Is your team the Kansas City Chiefs?")
                    wincondition = input()

                    while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            wincondition = input()

                elif winseason.lower().strip() == "no":
                        print("Do they play in one of the original 13 colonies?")#Asks the team
                        colonyyesorno = input()

                        while colonyyesorno.lower().strip() != "yes" and colonyyesorno.lower().strip() != "no":#Loops if not acceptable
                            print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                            colonyyesorno = input()
    
                        if colonyyesorno.lower().strip() == "no":
                            print("Is your team the Las Vegas Raiders?")#Asks the team
                            wincondition = input()
                            
                            while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                                print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                                wincondition = input()
                                
                        elif colonyyesorno.lower().strip() == "yes":
                            print("Is your team the New England Patriots?")#Asks the team
                            wincondition = input()

                            while wincondition.lower().strip() != "yes" and wincondition.lower().strip() != "no":#Loops if not acceptable
                                    print("ANSWER YES OR NO!!! I'M TOO TIRED TO PLAY THESE GAMES!")
                                    wincondition = input()

                
        
        
elif int(sprbwlwins) <= 1 and int(sprbwlwins) > -1:#Checks if the superbowl wins is in the range of 0 - 1
    print("Your team did worse than half of the league!")
    print("What conference does your team play in? The AFC or NFC?")
    conference = input()
#The below is all a joke
    while conference.lower().strip() != "nfc" and conference.lower().strip() != "afc":# When the answer isn't either, it loops
        print("What conference is your team in?")
        conference = input()

    if conference.strip().lower() == "nfc":  #Asks the team
        print("Is your team the Chicago Bears?")
        bears = input()

        while bears.lower().strip() != "yes" and bears.lower().strip() != "no":# When the answer isn't either, it loops
            print("Please respond yes or no!")
            bears = input()

        if bears == "yes":
            print("LETS GO!!!!")
            wincondition = "yes"

        else:
            print("Why didn't you read the instructions!!!")
            wincondition = "ish"
        
        
        
    elif conference.strip().lower() == "afc":  #Asks the team
        print("Is your team the Chicago Bears?")
        bears = input()

        while bears.lower().strip() != "yes" and bears.lower().strip() != "no":# When the answer isn't either, it loops
            print("Please respond yes or no!")
            bears = input()
            
        if bears == "yes":
            print("LETS GO!!!!")
            wincondition = "yes"

        else:
            print("Why didn't you read the instructions!!!")
            wincondition = "ish"
            

            
                

if wincondition.lower().strip() == "yes":#Finishes the code if the model guessed correctly!

    print("Thanks so much for playing!")
    print("Come back at another time to see if you can break the program!")
    
elif wincondition.lower().strip() == "no":#Finishes the code if the model failed
    print("Well done!!! You beat this game!")
    print("If you want to share this achievement with your friends,")
    print("you have to give me your social security number and bank")
    print("account!")
    bankinfo = input("> ")
elif wincondition == "ish":#If they failed
    print("Try again later.")
    print("Bye!")

if bankinfo and bankinfo.lower() == "bearswillwinthesuperbowl":#SHHHHHHHHHHHHH!!!
    print("Good job! Keep hating on the Packers!")



    
