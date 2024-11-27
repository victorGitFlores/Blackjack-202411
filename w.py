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
            bet_amt = int(input("How much you wanna bet? "))
            print(bet_amt)
            if bet_amt:
                if not my_chips.set_bet(bet_amt):
                    print("not enough chips!")
                else:
                    return bet_amt
        except:
            print("Try again")

#-------------------------------------------------------------------------------#
# in blackjack, the deck is never empty...if it empties, we start a new one
def hit(deck, hand):
#-------------------------------------------------------------------------------#   
    my_card = deck.deal_one()
    if my_card:
        hand.add_card(my_card)
        # if good totals, return True, if bust (over 21), return False
        return (hand.value1 <= 21 or hand.value11 <= 21) 

#-------------------------------------------------------------------------------#   
def hit_or_stand(deck, hand, player_or_dealer):
#-------------------------------------------------------------------------------#   
    global playing
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
        if hit(deck, hand):
            return True      # method returns True when player <= 21
        else:
            return False     # method returns False player over 21
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
    
    print("* ------------------------- *")
    print("Dealer cards: ")
    print("* ------------------------- *")
    for index, card in enumerate(hand_dealer.cards):
        card.print_card(True) if index != 0 else card.print_card(False)
            
#-------------------------------------------------------------------------------#   
def show_all(hand_player, hand_dealer):
#-------------------------------------------------------------------------------#   
    '''print all cards, except dealer's first'''
    print("* ------------------------- *")
    print("Player cards: ")
    print("* ------------------------- *")
    for card in hand_player.cards:
        card.print_card(True)
    print(f"Tot val  1: {hand_player.value1}")
    print(f"Tot val 11: {hand_player.value11}")
    
    print("* ------------------------- *")
    print("Dealer cards: ")
    print("* ------------------------- *")
    for card in hand_dealer.cards:
        card.print_card(True)
    print(f"Tot val  1: {hand_dealer.value1}")
    print(f"Tot val 11: {hand_dealer.value11}")
    

#-------------------------------------------------------------------------------#
def player_busts(hand_player, chips):
    ''' check for player bust/act on it Return True/False'''
#-------------------------------------------------------------------------------#   
    # if player exceeds 21...busted
    if (hand_player.value1 > 21 and hand_player.value11 > 21):
        chips.lose_bet()
        return True
    else:
        return False


#-------------------------------------------------------------------------------#
def hi_two_cons(val1, val2):
#-------------------------------------------------------------------------------#
    ''' highest of two constrained values. constraint? <= 21  '''
    hi_val = 0
    con1 = val1 if val1 <= 21 else 0
    con2 = val2 if val2 <= 21 else 0
    hi_val = con1 if con1 > con2 else con2
    return hi_val 

#-------------------------------------------------------------------------------#
def player_wins(hand_player, hand_dealer, chips):
#-------------------------------------------------------------------------------#
    ''' check for player win/act on it Return True/False'''
    # yeah, but what if player can still play some more? maybe has 14 and wants to go again?
    #  he cant 'win' more than once!
    # player_value? 
    player_value = hi_two_cons(hand_player.value1, hand_player.value11)    
    # dealer_value? 
    dealer_value = hi_two_cons(hand_dealer.value1, hand_dealer.value11)

    if (player_value > dealer_value):
        chips.win_bet()
        return True
    return False  #no need for else cause of the above return.


# mainline----------------------------------------------------------------------#

# set up player chips...
my_chips = classChips.Chips()
print(f"Before: {my_chips.total}")

# get validated bet amt...
bet_amt = take_bet(my_chips)
print(f"bet for {bet_amt} has been placed!")

# start a deck...
game_deck = classDeck.Deck()

# start a hand...
hand_player = classHand.Hand()
hand_dealer = classHand.Hand()
# before stats...
print("bef deck cards...", len(game_deck.deck_stack))
print("bef hand cards...", len(hand_player.cards))

# take a hit...
#hit(game_deck, hand_player)
# ask player for hit/stand...act on it
hit_or_stand(game_deck, hand_player, "Player")
#below 3 for testing... need cards in them hands!
hit_or_stand(game_deck, hand_player, "Player")
hit_or_stand(game_deck, hand_player, "Player")
#hit_or_stand(game_deck, hand_player, "Player")
hit_or_stand(game_deck, hand_dealer, "Dealer") # not sure if this applies to dealer... if so, then gotta pass 'dealer' or 'player' too, no?
hit_or_stand(game_deck, hand_dealer, "Dealer") # not sure if this applies to dealer... if so, then gotta pass 'dealer' or 'player' too, no?
hit_or_stand(game_deck, hand_dealer, "Dealer") # not sure if this applies to dealer... if so, then gotta pass 'dealer' or 'player' too, no?


# after stats...
print("aft deck cards...", len(game_deck.deck_stack))
print("aft hand cards...", len(hand_player.cards))

# testing: show the cards...
#show_some(hand_player, hand_dealer)
print("show all....")
show_all(hand_player, hand_dealer)


# is this a player bust?
#print("player bust? ", player_busts(hand_player, my_chips))
# does player win?
print("Player wins: ", player_wins(hand_player, hand_dealer, my_chips))




# critical var, used within local methods as global
playing = True