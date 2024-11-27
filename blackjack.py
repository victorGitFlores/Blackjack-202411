#blackjack.py
#-------------------------------------------------------------------------------#
import classCard
import classChips
import classDeck
import classHand
#-------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------#
def take_bet(my_chips):
#-------------------------------------------------------------------------------#
    ''' ask player for bet, check player has enough in chips
    '''
    while True:
        try:
            bet_amt = int(input("How much you wanna bet? (0 to quit) "))
            if bet_amt == 0:
                return bet_amt # wants to quit
            elif not my_chips.set_bet(bet_amt):
                print("Not enough chips")
            else:
                return bet_amt
        except:
            print("Try again")

#-------------------------------------------------------------------------------#
# in blackjack, the deck is never empty...if it empties, we start a new one
# if you ask for a hit, you get a card...returns True
def hit(deck, hand):
#-------------------------------------------------------------------------------#   
    my_card = deck.deal_one()
    if my_card:
        hand.add_card(my_card)
        return True
        
#-------------------------------------------------------------------------------#   
def hit_or_stand(deck, hand, player_or_dealer):
#-------------------------------------------------------------------------------#   

    val_hit   = ["Hit","hit","HIT", "Hit me", "hit me", "HIT ME", "Hit me!", "hit me!", "HIT ME!"]
    val_stand = ["Stand","stand","STAND"]

    while True:
        player_move = input(f" Hey, {player_or_dealer}, hit or stand?")
        #val...
        if player_move in val_hit + val_stand:
            break
        else:
            print("Not valid, Try again...")

    # do it... hit or stand
    if player_move in val_hit:
        return hit(deck, hand)  # will always be True! (ask for hit? get a hit!)
    elif player_move in val_stand:
        playing = False

#-------------------------------------------------------------------------------#   
def show_some(hand_player, hand_dealer):
#-------------------------------------------------------------------------------#   
    '''print all cards, except dealer's first'''
    print("* ------------------------- *")
    print("Player cards: ")
    print("* ------------------------- *")
    for card in hand_player.cards:
        card.print_card(True)
    player_tot_val = hi_two_cons(hand_player.value1, hand_player.value11)
    print(f"Total Player hand value: {player_tot_val}")
    print("* ------------------------- *")
    
    print("* ----- *")
    print("* ----- *")
    print("* ----- *")

    print("* ------------------------- *")
    print("Dealer cards: ")
    print("* ------------------------- *")
    for index, card in enumerate(hand_dealer.cards):
        card.print_card(True) if index != 0 else card.print_card(False)

    dealer_tot_val = hi_two_cons(hand_dealer.value1, hand_dealer.value11)
    print(f"Total Daler hand value: {dealer_tot_val}")
    print("* ------------------------- *")
    
    print("")
    print("")
    print("")
            
#-------------------------------------------------------------------------------#   
def show_all(hand_player, hand_dealer):
#-------------------------------------------------------------------------------#   
    '''print all cards, except dealer's first'''
    print("* ------------------------- *")
    print("Player cards: ")
    print("* ------------------------- *")
    for card in hand_player.cards:
        card.print_card(True)
    player_tot_val = hi_two_cons(hand_player.value1, hand_player.value11)
    print(f"Total Player hand value: {player_tot_val}")
    print("* ------------------------- *")    
    print("* ----- *")
    print("* ----- *")
    print("* ----- *")

    
    print("* ------------------------- *")
    print("Dealer cards: ")
    print("* ------------------------- *")
    for card in hand_dealer.cards:
        card.print_card(True)

    dealer_tot_val = hi_two_cons(hand_dealer.value1, hand_dealer.value11)
    print(f"Total Daler hand value: {dealer_tot_val}")
    print("* ------------------------- *")
    
    print("")
    print("")
    print("")
    



#-------------------------------------------------------------------------------#
def hi_two_cons(val1, val2):
#-------------------------------------------------------------------------------#
    ''' highest of two constrained values. constraint? <= 21  '''
    ''' if it returns zero, it means bust! (result is over constraint!) '''
    hi_val = 0
    con1 = val1 if val1 <= 21 else 0
    con2 = val2 if val2 <= 21 else 0
    hi_val = con1 if con1 > con2 else con2
    return hi_val 

#-------------------------------------------------------------------------------#
def player_busts(hand_value, chips):
    ''' check for player bust/act on it Return True/False'''
#-------------------------------------------------------------------------------#   
    # if player exceeds 21...busted
    if (hand_value == 0):
        chips.lose_bet()
        return True
    else:
        return False

#-------------------------------------------------------------------------------#
def player_wins(hand_player, hand_dealer, chips):
#-------------------------------------------------------------------------------#
    ''' check for player win/act on it Return True/False'''
    # player_value? 
    player_value = hi_two_cons(hand_player.value1, hand_player.value11)    
    # dealer_value? 
    dealer_value = hi_two_cons(hand_dealer.value1, hand_dealer.value11)

    if (player_value > dealer_value):
        chips.win_bet()
        return True
    return False  #no need for else cause of the above return.



#-------------------------------------------------------------------------------#
def dealer_wins(hand_player, hand_dealer, chips):
#-------------------------------------------------------------------------------#
    ''' check for dealer win/(nothing to do if so, besides...) return True/False'''
    # player_value? 
    player_value = hi_two_cons(hand_player.value1, hand_player.value11)    
    # dealer_value? 
    dealer_value = hi_two_cons(hand_dealer.value1, hand_dealer.value11)

    if (dealer_value > player_value):
        chips.lose_bet()
        return True
    return False  #no need for else cause of the above return.

#-------------------------------------------------------------------------------#
def push(hand_player, hand_dealer): # checks for tie
#-------------------------------------------------------------------------------#
    ''' check for tie... return True/False'''
    # player_value? 
    player_value = hi_two_cons(hand_player.value1, hand_player.value11)    
    # dealer_value? 
    dealer_value = hi_two_cons(hand_dealer.value1, hand_dealer.value11)

    if (dealer_value == player_value and player_value != 0):
        return True
    return False  #no need for else cause of the above return.

#-------------------------------------------------------------------------------#
def prompt_hit_stand(): # Prompts/returns 'hit' or 'stand' (valid_hit, valid_stand)
#-------------------------------------------------------------------------------#
    while True:
        hit_stand = input("Hit or stand?")
        if hit_stand in valid_hit + valid_stand:
            return hit_stand
        print("Try again...")

#-------------------------------------------------------------------------------#
def game_kickoff(cards_player, cards_dealer,player_chips): #returns False if they dont wanna bet
#-------------------------------------------------------------------------------#
    cards_player.reset_hand()
    cards_dealer.reset_hand()

    # round 1:
    cards_player.add_card(the_deck.deal_one())
    cards_dealer.add_card(the_deck.deal_one())
    # round 2:
    cards_player.add_card(the_deck.deal_one())
    cards_dealer.add_card(the_deck.deal_one())

    
    # Prompt the Player for their bet
    player_bet_amt = take_bet(player_chips)
    # but wait... if he ran out of chips...game over!
    if player_bet_amt == 0:
        print("Player not betting")
        return False
    
    # Show cards (but keep one dealer card hidden)
    show_some(cards_player, cards_dealer)
    return True

#-------------------------------------------------------------------------------#
def chk_win_sce(cards_player, cards_dealer, player_chips): #check winning scenarios
#-------------------------------------------------------------------------------#
    # run different winning scenarios...
    # a tie?
        if push(cards_player, cards_dealer):
            print("this was a tie!")
            return 'Tie'
    # player win?
        if player_wins(cards_player, cards_dealer, player_chips):
             print("Player won!")
             return 'Pla'
    # dealer win?
        if dealer_wins(cards_player, cards_dealer, player_chips):
            print("Dealer won!")
            return 'Dea'
    # no tie/no win
        return 'Non'




# mainline----------------------------------------------------------------------#

playing = True 

valid_hit = ["hit","Hit"]
valid_stand = ["stand","Stand"]
valid_yes = ["Yes","yes","Y","y"]
valid_no = ["No","no","N","n"]

# Print an opening statement
print("Welcome to the Black Parade Casino...")
# Create & shuffle the deck
the_deck = classDeck.Deck()
# Set up the Player's chips
player_chips = classChips.Chips()
cards_player = classHand.Hand()
cards_dealer = classHand.Hand()


while playing:

    # subgames are the games within 'playing'
    subgame = True
    if not game_kickoff(cards_player, cards_dealer,player_chips):
        playing = False
        print("Game over!")
        break

    #--------------------------------------------------------------------->
    # if both have 21, tie.
    # if player 21, player wins...if dealer 21, dealer wins (player loses).
    player_tot_val = hi_two_cons(cards_player.value1, cards_player.value11)
    dealer_tot_val = hi_two_cons(cards_dealer.value1, cards_dealer.value11)
    # tie:
    if player_tot_val == 21 and player_tot_val == dealer_tot_val: 
        print("Game over, this was a blackjackie tie!")
        subgame = False
    # player win:
    elif player_tot_val == 21:
        player_chips.win_bet()
        print("Game over, Player won!")
        subgame = False
    # dealer win (player loses):
    elif dealer_tot_val == 21:
        player_chips.lose_bet()
        print("Game over, Dealer won!")
        subgame = False

    #--------------------------------------------------------------------->
    # Prompt for Player to Hit or Stand
    #--------------------------------------------------------------------->
    if subgame:
        action_complete = False
        while not action_complete:
            hit_stand = prompt_hit_stand()
            print(f"at 002 {hit_stand}")
            if hit_stand in valid_hit:
                cards_player.add_card(the_deck.deal_one())
                player_tot_val = hi_two_cons(cards_player.value1, cards_player.value11)
                # show all cards (except dealer first...)
                print("at 001")
                show_some(cards_player, cards_dealer)

                if player_busts(player_tot_val, player_chips):                    
                    action_complete = True # bust!
            else:
                action_complete = True # stand
        
        # after action complete...
        # if player is 21...player wins, game over
        player_tot_val = hi_two_cons(cards_player.value1, cards_player.value11)
        
        dealer_turn = True
        
        if player_tot_val == 21:
            win_bet(player_chips)
            print("Player won with blackjack!")
            dealer_turn = False
        # if player over 21...busted, player loses, game over
        if player_tot_val == 0:
            player_chips.lose_bet()
            print("Player busted out!")
            dealer_turn = False
        #---------------------------------------------------------------------<

        #--------------------------------------------------------------------->
        
        if dealer_turn:
            # now it's the dealer's show...
            print("now its dealer turn... will hit at <= 17!")
            #If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            dealer_tot_val = hi_two_cons(cards_dealer.value1, cards_dealer.value11)
            #player has quit turn (stand, or bust...) #if dealer over >=17...could be over now!
            
            if dealer_tot_val >= 17:
                game_status = chk_win_sce(cards_player, cards_dealer, player_chips) #check winning scenarios...
            
            #but if dealer < 17...dealer's turn...
            while dealer_tot_val < 17 and dealer_tot_val > 0:
                cards_dealer.add_card(the_deck.deal_one())
                dealer_tot_val = hi_two_cons(cards_dealer.value1, cards_dealer.value11)
                # Show all cards
                show_all(cards_player, cards_dealer)
                # dealer bust?
                if dealer_tot_val == 0:
                    print("dealer bust! ! !")
                    player_wins(cards_player, cards_dealer, player_chips)

            game_status = chk_win_sce(cards_player, cards_dealer, player_chips) #check winning scenarios...


    #--------------------------------------------------------------------->

    #---------------------------------------------------------------------<
    # inform player of their chip total...
    print(f"CURRENT PLAYER CHIP TOTAL: {player_chips.total}")

    # Ask to play again

    again = True
    while again:
        yes_no = input("Play again?")
        if yes_no in valid_yes + valid_no:
            break
    if yes_no in valid_no:
        playing = False
        print("Game over!")
            
