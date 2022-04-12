# wheel of fortune game rules/set up:


                        # player/round 
# 3 players
# first 2 rounds including all players
# spin the wheel (select spin)
# if wheel lands on $$$ guess a consonant

#////////////////////////////////////////////////////////////////////////////////

                    # set up values for wheel

#consonant = B, C, D, F, G, J, K, L, M, N, P, Q, S, T, V, X, Z, H, R, W, Y
#vowels = A, E, I, O, U

# def wheel_value():
    #wheel_choices = ("bankrupt", "lose a turn", "$50,...")
    #wheel_value = random.choice(wheel_choices)
    #return wheel_value

#////////////////////////////////////////////////////////////////////////////////

                    # spinning wheel

# user prompted with:
    # spin the wheel feature (type spin to spin wheel)
    # guess word 

# display what the user spun (result of spin)

                    # after spin

# if wheel_choice is LOSE A TURN
    # end turn

# if wheel_choice is BANKRUPT
    # BANK_TOTAL = 0
    #end turn

# if wheel_choice is not LOSE A TURN AND BANKRUPT
    # input user guess (enter a consonant)
        # if user input guess is not in consonant list 
            #print guess is not consonant
            #if user input is in consonant list 
             # add money to round amount
                #Use this code to show user the position of guess in phrase
                            # (CHANGE VARIABLES)
                # for position in range(len(word)):
                #                 if word[position] == user_input: 
                #                     word_list[position] = user_input

                #if BANK_TOTAL >= 250
                    #prompt user if they would like to buy a vowel
                        # USE a vowel function
                #else 
                    #end turn

#////////////////////////////////////////////////////////////////////////////////

# successful guess = ability to buy vowels
    # if money >= vowel_charge 
    #   vowel_ability = True
    #   subtract vowel_charge from player(x)_total 
    # else 
    #   end turn, move to the next person


        #final round
# final round (round 3) is the player w the highest bank amount $$$ 
# rev
# game ends after round 3
#



        #the wheel
#24 segments
# 1 BANKRUPT
# 1 lose a turn
# rest are money values $50 - $900

