import random
import time

#HAVE TO TYPE IN CAPS

# Time 
# def countdown(time_sec):
#     while time_sec:
#         mins, secs = divmod(time_sec, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         time_sec -= 1

#     print("TIMES UP!")

# wheel values
def value():
    wheel_choices = ("BANKRUPT", "LOSE A TURN", 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900)
    wheel_value = random.choice(wheel_choices)
    return wheel_value


# letter bank
consonant = ('B','C','D','F','G','J','K','L','M','N','P','Q','S','T','V','X','Z','H','R','W','Y')
vowels = ('A','E','I','O','U')

stored_consonant =[]
stored_vowels = []

# words
file = (r"words2.txt") 

#declaring a word to guess
def puzzle_file():
    word_file = open(file)
    word_choice = random.choice(word_file.read().split())
    word_file.close()
    return word_choice

# hidden_list = []

    # adds _'s to each letter of the word

def hidden_list_reset(puzzle):
    hidden_list_diff = []
    for char in puzzle:
        hidden_list_diff.append("_")
    print(hidden_list_diff)
    return hidden_list_diff
        


# the players ability to play
player1_turn = True
player2_turn = False
player3_turn = False

# amount of money per player
player1_bank_r1 = 0
player2_bank_r1 = 0
player3_bank_r1 = 0
#round 2
player1_bank_r2 = 0
player2_bank_r2 = 0
player3_bank_r2 = 0
#final round
player1_bank = player1_bank_r1 + player1_bank_r2
player2_bank = player2_bank_r1 + player2_bank_r2
player3_bank = player3_bank_r1 + player3_bank_r2
# Final round variables

final_attempt = 5
prize_third_round = 25000
prize_winner = 0

# ranks the players banks and gets the highest amount and shows the leader
player_bank_list = player1_bank, player2_bank, player3_bank
rank1_player = max(player_bank_list)


spin_wheel = True
round1 = True
round2 = False
round3 = False

final_attempt_status = True


while round1 == True:
    puzzle = puzzle_file()
    hidden_list = hidden_list_reset(puzzle)
    print(puzzle)
    print(hidden_list)
    print("Round One!")

    while player1_turn == True:
        print("Player One, ")

        #gets the decision by player
        wheel_decision = input("Would you like to spin the Wheel of Fortune? (Yes/No): ")
        
        if wheel_decision == "Yes":
            #grabs value from function for wheel values
            result_of_wheel = value()            
            print("This is the result of your spin!!")
            print(":", result_of_wheel)

            if isinstance(result_of_wheel, int):

                player1_bank_r1 = player1_bank_r1 + result_of_wheel
                print("Balance: $", player1_bank_r1)
                print("The word to guess is: ", hidden_list)

                # user gets to guess a consonant
                consonant_guess = input("Guess a CONSONANT: ")
                if consonant_guess in consonant:
                    print("Consonant:",consonant_guess)

                    if consonant_guess in puzzle:
                        stored_consonant.append(consonant_guess)
                        print(stored_consonant)
                        # consonant.pop(consonant_guess)

                        # shows user the where the consonant is within the word
                        for position in range(len(puzzle)):
                            if puzzle[position] == consonant_guess: 
                                hidden_list[position] = consonant_guess

                                # user is allowed to buy a vowel if able
                            
                    else:
                        print("Sorry,",consonant_guess, "is not in the word.")
                        player1_bank_r1 = player1_bank_r1 - result_of_wheel
                        player1_turn = False
                        player2_turn = True
                    

                else:
                    print("Sorry,",consonant_guess, "is not a consonant.")                    
                    player1_bank_r1 = player1_bank_r1 - result_of_wheel
                print(hidden_list)

                if player1_bank_r1 >= 250:
                    buy_vowel = input("Would you like to buy a vowel?(Yes/No):")

                    if buy_vowel == "Yes":
                        player1_bank_r1 = player1_bank_r1 -250
                        vowel_guess = input("Guess a VOWEL: ")
                        if vowel_guess in vowels:
                            print("Vowel:",vowel_guess)
                            if vowel_guess in puzzle:
                                print("")
                                stored_vowels.append(vowel_guess)
                                print("Vowels guessed:", stored_vowels)
                                # consonant.pop(consonant_guess)

                                # shows user the where the consonant is within the word
                                for position in range(len(puzzle)):
                                    if puzzle[position] == vowel_guess: 
                                        hidden_list[position] = vowel_guess
                                        print(hidden_list)

                                        player1_turn = False
                                        player2_turn = True
                            else:
                                print("Sorry,",vowel_guess, "is not in the word.")

                                player1_turn = False
                                player2_turn = True
                        else:
                            print("Sorry,",vowel_guess, "is not a vowel.")

                            player1_turn = False
                            player2_turn = True

                    elif buy_vowel == "No":
                        print("Alright, next player!")

                        player1_turn = False
                        player2_turn = True

                print("Next player!")
                player1_turn = False
                player2_turn = True

            # user result is bankrupt = total goes to 0
            elif result_of_wheel == "BANKRUPT":
                player1_turn = False
                player1_bank_r1 = 0
                print("I'm sorry... you lost everything in your bank!!")
                print("Balance: $", player1_bank_r1)
                print("Next player! ")
                player2_turn = True

            # user loses their turn
            elif result_of_wheel == "LOSE A TURN":
                player1_turn = False
                print("You lost your turn, next player!")
                player2_turn = True


        elif wheel_decision == "No":
            guess_word = input("Would you like to guess the word? (Yes/No): ")

            if guess_word == "Yes":
                guess_word_attempt = input("Guess the word: ")
                print("Guess was: ", guess_word_attempt)
                
                if guess_word_attempt == puzzle:

                    print("You guessed the word!!")
                    print("Next Round!")

                    player2_bank_r1 = 0
                    player3_bank_r1 = 0 

                    print("Player 1 Bank: $", player1_bank_r1)
                    print("Player 2 Bank: $", player2_bank_r1)
                    print("Player 3 Bank: $", player3_bank_r1)
                    player1_turn = False
                    player2_turn = False
                    player3_turn = False
                    round1 = False
                    round2 = True
                else:
                    print("sorry incorrect...")
                    
            if guess_word == "No":
                print("Next player! ")
                player1_turn = False
                player2_turn = True
        
        else:
            print("Please select 'Yes' or 'No'")
    while player2_turn == True:
        print("Player Two, ")

        #gets the decision by player
        wheel_decision = input("Would you like to spin the Wheel of Fortune? (Yes/No): ")
        
        if wheel_decision == "Yes":
            #grabs value from function for wheel values
            result_of_wheel = value()            
            print("This is the result of your spin!!")
            print(":", result_of_wheel)

            if isinstance(result_of_wheel, int):

                player2_bank_r1 = player2_bank_r1 + result_of_wheel
                print("Balance: $", player2_bank_r1)
                print("The word to guess is: ", hidden_list)

                # user gets to guess a consonant
                consonant_guess = input("Guess a CONSONANT: ")
                if consonant_guess in consonant:
                    print("Consonant:",consonant_guess)

                    if consonant_guess in puzzle:
                        stored_consonant.append(consonant_guess)
                        print(stored_consonant)
                        # consonant.pop(consonant_guess)

                        # shows user the where the consonant is within the word
                        for position in range(len(puzzle)):
                            if puzzle[position] == consonant_guess: 
                                hidden_list[position] = consonant_guess

                                # user is allowed to buy a vowel if able
                            
                    else:
                        print("Sorry,",consonant_guess, "is not in the word.")
                        player2_bank_r1 = player2_bank_r1 - result_of_wheel
                        player2_turn = False
                        player3_turn = True
                    

                else:
                    print("Sorry,",consonant_guess, "is not a consonant.")                    
                    player2_bank_r1 = player2_bank_r1 - result_of_wheel
                print(hidden_list)

                if player2_bank_r1 >= 250:
                    buy_vowel = input("Would you like to buy a vowel?(Yes/No):")

                    if buy_vowel == "Yes":
                        player2_bank = player2_bank -250
                        vowel_guess = input("Guess a VOWEL: ")
                        if vowel_guess in vowels:
                            print("Vowel:",vowel_guess)
                            if vowel_guess in puzzle:
                                print("")
                                stored_vowels.append(vowel_guess)
                                print("Vowels guessed:", stored_vowels)
                                # consonant.pop(consonant_guess)

                                # shows user the where the consonant is within the word
                                for position in range(len(puzzle)):
                                    if puzzle[position] == vowel_guess: 
                                        hidden_list[position] = vowel_guess
                                        print(hidden_list)

                                        player2_turn = False
                                        player3_turn = True
                            else:
                                print("Sorry,",vowel_guess, "is not in the word.")

                                player2_turn = False
                                player3_turn = True
                        else:
                            print("Sorry,",vowel_guess, "is not a vowel.")

                            player2_turn = False
                            player3_turn = True

                    elif buy_vowel == "No":
                        print("Alright, next player!")

                        player2_turn = False
                        player3_turn = True

                print("Next player!")
                player2_turn = False
                player3_turn = True

            # user result is bankrupt = total goes to 0
            elif result_of_wheel == "BANKRUPT":
                player2_turn = False
                player2_bank_r1 = 0
                print("I'm sorry... you lost everything in your bank!!")
                print("Balance: $", player2_bank_r1)
                print("Next player! ")
                player3_turn = True

            # user loses their turn
            elif result_of_wheel == "LOSE A TURN":
                print("You lost your turn, next player!")
                player2_turn = False
                player3_turn = True


        elif wheel_decision == "No":
            guess_word = input("Would you like to guess the word? (Yes/No): ")

            if guess_word == "Yes":
                guess_word_attempt = input("Guess the word: ")
                print("Guess was: ", guess_word_attempt)
                
                if guess_word_attempt == puzzle:
                  
                    print("You guessed the word!!")
                    print("Next Round!")

                    player1_bank_r1 = 0
                    player3_bank_r1 = 0 

                    print("Player 1 Bank: $", player1_bank_r1)
                    print("Player 2 Bank: $", player2_bank_r1)
                    print("Player 3 Bank: $", player3_bank_r1)
                    player1_turn = False
                    player2_turn = False
                    player3_turn = False
                    round1 = False
                    round2 = True  
                else:
                    print("sorry incorrect...")
            if guess_word == "No":
                print("Next player! ")
                player2_turn = False
                player3_turn = True
        
        else:
            print("Please select 'Yes' or 'No'")
    while player3_turn == True:
        print("Player Three, ")

        #gets the decision by player
        wheel_decision = input("Would you like to spin the Wheel of Fortune? (Yes/No): ")
        
        if wheel_decision == "Yes":
            #grabs value from function for wheel values
            result_of_wheel = value()
            print("This is the result of your spin!!")
            print(":", result_of_wheel)

            if isinstance(result_of_wheel, int):

                player3_bank_r1 = player3_bank_r1 + result_of_wheel
                print("Balance: $", player3_bank_r1)
                print("The word to guess is: ", hidden_list)

                # user gets to guess a consonant
                consonant_guess = input("Guess a CONSONANT: ")
                if consonant_guess in consonant:
                    print("Consonant:",consonant_guess)

                    if consonant_guess in puzzle:
                        stored_consonant.append(consonant_guess)
                        print(stored_consonant)
                        # consonant.pop(consonant_guess)

                        # shows user the where the consonant is within the word
                        for position in range(len(puzzle)):
                            if puzzle[position] == consonant_guess: 
                                hidden_list[position] = consonant_guess

                                # user is allowed to buy a vowel if able
                            
                    else:
                        print("Sorry,",consonant_guess, "is not in the word.")
                        player3_bank_r1 = player3_bank_r1 - result_of_wheel
                        player3_turn = False
                        player1_turn = True
                    

                else:
                    print("Sorry,",consonant_guess, "is not a consonant.")                    
                    player3_bank_r1 = player3_bank_r1 - result_of_wheel
                print(hidden_list)

                if player3_bank_r1 >= 250:
                    buy_vowel = input("Would you like to buy a vowel?(Yes/No):")

                    if buy_vowel == "Yes":
                        player3_bank_r1 = player3_bank_r1 -250
                        vowel_guess = input("Guess a VOWEL: ")
                        if vowel_guess in vowels:
                            print("Vowel:",vowel_guess)
                            if vowel_guess in puzzle:
                                print("")
                                stored_vowels.append(vowel_guess)
                                print("Vowels guessed:", stored_vowels)
                                # consonant.pop(consonant_guess)

                                # shows user the where the consonant is within the word
                                for position in range(len(puzzle)):
                                    if puzzle[position] == vowel_guess: 
                                        hidden_list[position] = vowel_guess
                                        print(hidden_list)

                                        player3_turn = False
                                        player1_turn = True
                            else:
                                print("Sorry,",vowel_guess, "is not in the word.")

                                player3_turn = False
                                player1_turn = True
                        else:
                            print("Sorry,",vowel_guess, "is not a vowel.")

                            player3_turn = False
                            player1_turn = True

                    elif buy_vowel == "No":
                        print("Alright, next player!")

                        player3_turn = False
                        player1_turn = True

                print("Next player!")
                player3_turn = False
                player1_turn = True

            # user result is bankrupt = total goes to 0
            elif result_of_wheel == "BANKRUPT":
                player3_turn = False
                player3_bank_r1 = 0
                print("I'm sorry... you lost everything in your bank!!")
                print("Balance: $", player3_bank_r1)
                print("Next player! ")
                player1_turn = True

            # user loses their turn
            elif result_of_wheel == "LOSE A TURN":
                print("You lost your turn, next player!")
                player3_turn = False
                player1_turn = True


        elif wheel_decision == "No":
            guess_word = input("Would you like to guess the word? (Yes/No): ")

            if guess_word == "Yes":
                guess_word_attempt = input("Guess the word: ")
                print("Guess was: ", guess_word_attempt)
                
                if guess_word_attempt == puzzle:
                   
                    print("You guessed the word!!")
                    print("Next Round!")

                    player1_bank_r1 = 0
                    player2_bank_r1 = 0 

                    print("Player 1 Bank: $", player1_bank_r1)
                    print("Player 2 Bank: $", player2_bank_r1)
                    print("Player 3 Bank: $", player3_bank_r1)

                    player1_turn = False
                    player2_turn = False
                    player3_turn = False
                    round1 = False
                    round2 = True
                else:
                    print("sorry incorrect...")

            if guess_word == "No":
                print("Next player! ")
                player3_turn = False
                player1_turn = True
        
        else:
            print("Please select 'Yes' or 'No'")

while round2 == True:
    puzzle = puzzle_file()
    hidden_list = hidden_list_reset(puzzle)
    print(puzzle)
    print(hidden_list)

    print("Round Two!")
    player1_turn = True
    while player1_turn == True:
        print("Player One, ")

        #gets the decision by player
        wheel_decision = input("Would you like to spin the Wheel of Fortune? (Yes/No): ")
        
        if wheel_decision == "Yes":
            #grabs value from function for wheel values
            result_of_wheel = value()            
            print("This is the result of your spin!!")
            print(":", result_of_wheel)

            if isinstance(result_of_wheel, int):

                player1_bank_r2 = player1_bank_r2 + result_of_wheel
                print("Round Balance: $", player1_bank_r2)
                print("The word to guess is: ", hidden_list)

                # user gets to guess a consonant
                consonant_guess = input("Guess a CONSONANT: ")
                if consonant_guess in consonant:
                    print("Consonant:",consonant_guess)

                    if consonant_guess in puzzle:
                        stored_consonant.append(consonant_guess)
                        print(stored_consonant)
                        # consonant.pop(consonant_guess)

                        # shows user the where the consonant is within the word
                        for position in range(len(puzzle)):
                            if puzzle[position] == consonant_guess: 
                                hidden_list[position] = consonant_guess

                                # user is allowed to buy a vowel if able
                            
                    else:
                        print("Sorry,",consonant_guess, "is not in the word.")
                        player1_bank_r2 = player1_bank_r2 - result_of_wheel
                        player1_turn = False
                        player2_turn = True
                    

                else:
                    print("Sorry,",consonant_guess, "is not a consonant.")                    
                    player1_bank_r2 = player1_bank_r2 - result_of_wheel
                print(hidden_list)

                if player1_bank_r2 >= 250:
                    buy_vowel = input("Would you like to buy a vowel?(Yes/No):")

                    if buy_vowel == "Yes":
                        player1_bank_r2 = player1_bank_r2 -250
                        vowel_guess = input("Guess a VOWEL: ")
                        if vowel_guess in vowels:
                            print("Vowel:",vowel_guess)
                            if vowel_guess in puzzle:
                                print("")
                                stored_vowels.append(vowel_guess)
                                print("Vowels guessed:", stored_vowels)
                                # consonant.pop(consonant_guess)

                                # shows user the where the consonant is within the word
                                for position in range(len(puzzle)):
                                    if puzzle[position] == vowel_guess: 
                                        hidden_list[position] = vowel_guess
                                        print(hidden_list)

                                        player1_turn = False
                                        player2_turn = True
                            else:
                                print("Sorry,",vowel_guess, "is not in the word.")

                                player1_turn = False
                                player2_turn = True
                        else:
                            print("Sorry,",vowel_guess, "is not a vowel.")

                            player1_turn = False
                            player2_turn = True

                    elif buy_vowel == "No":
                        print("Alright, next player!")

                        player1_turn = False
                        player2_turn = True

                print("Next player!")
                player1_turn = False
                player2_turn = True

            # user result is bankrupt = total goes to 0
            elif result_of_wheel == "BANKRUPT":
                player1_turn = False
                player1_bank_r2 = 0
                print("I'm sorry... you lost everything in your bank!!")
                print("Balance: $", player1_bank_r2)
                print("Next player! ")
                player2_turn = True

            # user loses their turn
            elif result_of_wheel == "LOSE A TURN":
                print("You lost your turn, next player!")
                player1_turn = False
                player2_turn = True


        elif wheel_decision == "No":
            guess_word = input("Would you like to guess the word? (Yes/No): ")

            if guess_word == "Yes":
                guess_word_attempt = input("Guess the word: ")
                print("Guess was: ", guess_word_attempt)
                
                if guess_word_attempt == puzzle:

                    print("You guessed the word!!")
                    print("Next Round!")

                    player2_bank_r2 = 0
                    player3_bank_r2 = 0 

                    print("Player 1 Bank: $", player1_bank_r2)
                    print("Player 2 Bank: $", player2_bank_r2)
                    print("Player 3 Bank: $", player3_bank_r2)
                    player1_turn = False
                    player2_turn = False
                    player3_turn = False
                    round2 = False
                    round3 = True
                else:
                    print("sorry incorrect...")
                    
            if guess_word == "No":
                print("Next player! ")
                player1_turn = False
                player2_turn = True
        
        else:
            print("Please select 'Yes' or 'No'")
    while player2_turn == True:
        print("Player Two, ")

        #gets the decision by player
        wheel_decision = input("Would you like to spin the Wheel of Fortune? (Yes/No): ")
        
        if wheel_decision == "Yes":
            #grabs value from function for wheel values
            result_of_wheel = value()            
            print("This is the result of your spin!!")
            print(":", result_of_wheel)

            if isinstance(result_of_wheel, int):

                player2_bank_r2 = player2_bank_r2 + result_of_wheel
                print("Balance: $", player2_bank_r2)
                print("The word to guess is: ", hidden_list)

                # user gets to guess a consonant
                consonant_guess = input("Guess a CONSONANT: ")
                if consonant_guess in consonant:
                    print("Consonant:",consonant_guess)

                    if consonant_guess in puzzle:
                        stored_consonant.append(consonant_guess)
                        print(stored_consonant)
                        # consonant.pop(consonant_guess)

                        # shows user the where the consonant is within the word
                        for position in range(len(puzzle)):
                            if puzzle[position] == consonant_guess: 
                                hidden_list[position] = consonant_guess

                                # user is allowed to buy a vowel if able
                            
                    else:
                        print("Sorry,",consonant_guess, "is not in the word.")
                        player2_bank_r2 = player2_bank_r2 - result_of_wheel
                        player2_turn = False
                        player3_turn = True
                    

                else:
                    print("Sorry,",consonant_guess, "is not a consonant.")                    
                    player2_bank_r2 = player2_bank_r2 - result_of_wheel
                print(hidden_list)

                if player2_bank_r2 >= 250:
                    buy_vowel = input("Would you like to buy a vowel?(Yes/No):")

                    if buy_vowel == "Yes":
                        player2_bank_r2 = player2_bank_r2 -250
                        vowel_guess = input("Guess a VOWEL: ")
                        if vowel_guess in vowels:
                            print("Vowel:",vowel_guess)
                            if vowel_guess in puzzle:
                                print("")
                                stored_vowels.append(vowel_guess)
                                print("Vowels guessed:", stored_vowels)
                                # consonant.pop(consonant_guess)

                                # shows user the where the consonant is within the word
                                for position in range(len(puzzle)):
                                    if puzzle[position] == vowel_guess: 
                                        hidden_list[position] = vowel_guess
                                        print(hidden_list)

                                        player2_turn = False
                                        player3_turn = True
                            else:
                                print("Sorry,",vowel_guess, "is not in the word.")

                                player2_turn = False
                                player3_turn = True
                        else:
                            print("Sorry,",vowel_guess, "is not a vowel.")

                            player2_turn = False
                            player3_turn = True

                    elif buy_vowel == "No":
                        print("Alright, next player!")

                        player2_turn = False
                        player3_turn = True

                print("Next player!")
                player2_turn = False
                player3_turn = True

            # user result is bankrupt = total goes to 0
            elif result_of_wheel == "BANKRUPT":
                player2_turn = False
                player2_bank_r2 = 0
                print("I'm sorry... you lost everything in your bank!!")
                print("Balance: $", player2_bank_r2)
                print("Next player! ")
                player3_turn = True

            # user loses their turn
            elif result_of_wheel == "LOSE A TURN":
                print("You lost your turn, next player!")
                player2_turn = False
                player3_turn = True


        elif wheel_decision == "No":
            guess_word = input("Would you like to guess the word? (Yes/No): ")

            if guess_word == "Yes":
                guess_word_attempt = input("Guess the word: ")
                print("Guess was: ", guess_word_attempt)
                
                if guess_word_attempt == puzzle:
                  
                    print("You guessed the word!!")
                    print("Next Round!")

                    player1_bank_r2 = 0
                    player3_bank_r2 = 0 

                    print("Player 1 Bank: $", player1_bank_r2)
                    print("Player 2 Bank: $", player2_bank_r2)
                    print("Player 3 Bank: $", player3_bank_r2)
                    player1_turn = False
                    player2_turn = False
                    player3_turn = False
                    round2 = False
                    round3 = True 
                else:
                    print("sorry incorrect...")

            if guess_word == "No":
                print("Next player! ")
                player2_turn = False
                player3_turn = True
        
        else:
            print("Please select 'Yes' or 'No'")
    while player3_turn == True:
        print("Player Three, ")

        #gets the decision by player
        wheel_decision = input("Would you like to spin the Wheel of Fortune? (Yes/No): ")
        
        if wheel_decision == "Yes":
            #grabs value from function for wheel values
            result_of_wheel = value()
            print("This is the result of your spin!!")
            print(":", result_of_wheel)

            if isinstance(result_of_wheel, int):

                player3_bank_r2 = player3_bank_r2 + result_of_wheel
                print("Balance: $", player3_bank_r2)
                print("The word to guess is: ", hidden_list)

                # user gets to guess a consonant
                consonant_guess = input("Guess a CONSONANT: ")
                if consonant_guess in consonant:
                    print("Consonant:",consonant_guess)

                    if consonant_guess in puzzle:
                        stored_consonant.append(consonant_guess)
                        print(stored_consonant)
                        # consonant.pop(consonant_guess)

                        # shows user the where the consonant is within the word
                        for position in range(len(puzzle)):
                            if puzzle[position] == consonant_guess: 
                                hidden_list[position] = consonant_guess

                                # user is allowed to buy a vowel if able
                            
                    else:
                        print("Sorry,",consonant_guess, "is not in the word.")
                        player3_bank_r2 = player3_bank_r2 - result_of_wheel
                        player3_turn = False
                        player1_turn = True
                    

                else:
                    print("Sorry,",consonant_guess, "is not a consonant.")                    
                    player3_bank_r2 = player3_bank_r2 - result_of_wheel
                print(hidden_list)

                if player3_bank_r2 >= 250:
                    buy_vowel = input("Would you like to buy a vowel?(Yes/No):")

                    if buy_vowel == "Yes":
                        player3_bank_r2 = player3_bank_r2 -250
                        vowel_guess = input("Guess a VOWEL: ")
                        if vowel_guess in vowels:
                            print("Vowel:",vowel_guess)
                            if vowel_guess in puzzle:
                                print("")
                                stored_vowels.append(vowel_guess)
                                print("Vowels guessed:", stored_vowels)
                                # consonant.pop(consonant_guess)

                                # shows user the where the consonant is within the word
                                for position in range(len(puzzle)):
                                    if puzzle[position] == vowel_guess: 
                                        hidden_list[position] = vowel_guess
                                        print(hidden_list)

                                        player3_turn = False
                                        player1_turn = True
                            else:
                                print("Sorry,",vowel_guess, "is not in the word.")

                                player3_turn = False
                                player2_turn = True
                        else:
                            print("Sorry,",vowel_guess, "is not a vowel.")

                            player3_turn = False
                            player1_turn = True

                    elif buy_vowel == "No":
                        print("Alright, next player!")

                        player3_turn = False
                        player1_turn = True

                print("Next player!")
                player3_turn = False
                player1_turn = True

            # user result is bankrupt = total goes to 0
            elif result_of_wheel == "BANKRUPT":
                player3_turn = False
                player3_bank_r2 = 0
                print("I'm sorry... you lost everything in your bank!!")
                print("Balance: $", player3_bank_r2)
                print("Next player! ")
                player1_turn = True

            # user loses their turn
            elif result_of_wheel == "LOSE A TURN":
                player3_turn = False
                print("You lost your turn, next player!")
                player3_turn = False
                player1_turn = True


        elif wheel_decision == "No":
            guess_word = input("Would you like to guess the word? (Yes/No): ")

            if guess_word == "Yes":
                guess_word_attempt = input("Guess the word: ")
                print("Guess was: ", guess_word_attempt)
                
                if guess_word_attempt == puzzle:
                   
                    print("You guessed the word!!")
                    print("Next Round!")

                    player2_bank_r2 = 0
                    player3_bank_r2 = 0

                    print("Player 1 Bank: $", player1_bank_r2)
                    print("Player 2 Bank: $", player2_bank_r2)
                    print("Player 3 Bank: $", player3_bank_r2)
                    player1_turn = False
                    player2_turn = False
                    player3_turn = False
                    round2 = False
                    round3 = True
                else:
                    print("sorry incorrect...")

            if guess_word == "No":
                print("Next player! ")
                player3_turn = False
                player1_turn = True
        
        else:
            print("Please select 'Yes' or 'No'")

while round3 == True:
    print("Final Round!")

    # new word to guess
    puzzle = puzzle_file()
    hidden_list = hidden_list_reset(puzzle)
    print(puzzle)
    print(hidden_list)
        

    # Grabs the winner of previous rounds
    if rank1_player == player1_bank:
        print("The player with the HIGHEST score is....player 1!" ,"$",player1_bank)

    elif rank1_player == player2_bank:
        print("The player with the HIGHEST score is....player 2!" ,"$",player2_bank)

    elif rank1_player == player3_bank:
        print("The player with the HIGHEST score is....player 3!" ,"$",player3_bank)



    # Shows the word to be guessed for the final
    print("Reveal 'R-S-T-L-N-E'!")

    letter1 = "R"
    letter2 = "S"
    letter3 = "T"
    letter4 = "L"
    letter5 = "E"

    # Goes through the word to see if it contains the given letters
    for position in range(len(puzzle)):
        if puzzle[position] == letter1:
            hidden_list[position] = letter1
        if puzzle[position] == letter2:
            hidden_list[position] = letter2        
        if puzzle[position] == letter3:
            hidden_list[position] = letter3       
        if puzzle[position] == letter4:
            hidden_list[position] = letter4
        if puzzle[position] == letter5:
            hidden_list[position] = letter5

    # Prints the given letters 
    print(hidden_list)

    # Lets user know what they can guess for the final word
    print("You are allowed 3 consonants and 1 vowel.")

    # This checks to see if user input a consonant and then a vowel
    consonant_check1 = False
    consonant_check2 = False
    consonant_check3 = False
    vowel_check = False

    # If valid it will go onto the next guess
    while consonant_check1 == False:
        
        # User gives a consonant
        consonant_final1 = input("Consonant 1: ")

        if consonant_final1 in consonant:
            print("Yes!")
            consonant_check1 = True 
        else:
            consonant_check1 = False
            print("Please enter a valid consonant.")    

    while consonant_check2 == False:

        # User gives a consonant
        consonant_final2 = input("Consonant 2: ")

        if consonant_final2 in consonant:
            print("Yes!")
            consonant_check2 = True 
        else:
            consonant_check2 = False
            print("Please enter a valid consonant.")  

    while consonant_check3 == False:

        # User gives a consonant
        consonant_final3 = input("Consonant 3: ")

        if consonant_final3 in consonant:
            print("Yes!")
            consonant_check3 = True 
        else:
            consonant_check3 = False
            print("Please enter a valid consonant.")   

    while vowel_check == False:

        # User gives vowel
        vowel_final = input("Vowel: ")

        if vowel_final in vowels:
            print("Yes!")
            vowel_check = True 
        else:
            vowel_check = False
            print("Please enter a valid vowel.")   

    # Checking if valid input
    # FIRST CONSONANT
    if consonant_final1 in puzzle:
        print("Consonant 1 is in the word!")
    elif consonant_final1 not in puzzle:
        print("Consonant 1 is NOT in the word!")

    # SECOND CONSONANT
    if consonant_final2 in puzzle:
        print("Consonant 2 is in the word!")  
    elif consonant_final2 not in puzzle:
        print("Consonant 2 is NOT in the word!") 

    # THIRD CONSONANT
    if consonant_final3 in puzzle:
        print("Consonant 3 is in the word!")
    elif consonant_final3 not in puzzle:
        print("Consonant 3 is NOT in the word!") 

    # VOWEL GUESS
    if vowel_final in puzzle:
        print("This vowel is in the word!")    
    elif vowel_final not in puzzle:
        print("This vowel is NOT in the word!") 

    for position in range(len(puzzle)):
        if puzzle[position] == consonant_final1:
            hidden_list[position] = consonant_final1
        if puzzle[position] == consonant_final2:
            hidden_list[position] = consonant_final2        
        if puzzle[position] == consonant_final3:
            hidden_list[position] = consonant_final3       
        if puzzle[position] == vowel_final:
            hidden_list[position] = vowel_final
    print(hidden_list)


# couldn't get timer to work properly, using attempts instead
    while final_attempt_status == True:

        if final_attempt > 0:
            print("You have", final_attempt,"attempt(s) to guess word!!")
            final_guesses = input("Guess: ")

            # Checks input if it is alpha
            check_input = final_guesses.isalpha()
            if final_guesses.isalpha():

                # User guessed word correct
                if final_guesses == puzzle:
                    print("YOU WON!!")
                    prize_winner = rank1_player + prize_third_round
                    print("CONGRADULATIONS!! YOU WON $", prize_winner, "!!")

                    final_attempt_status = False
                    round3 = False
                    round2 = False
                    round1 = False
                    

                elif final_guesses != puzzle:
                    print("Nope, try again!!")
                    final_attempt = final_attempt - 1
            else:
                print("Please input valid characters!")

        # Once attempts are used up
        if final_attempt == 0:
            round3 = False
            round2 = False
            round1 = False
            print("I'm sorry you lost.")
            print("The word was: ", puzzle)

