#w2.py

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
def get_hand_val(val1, val11): #returns hand value
#-------------------------------------------------------------------------------#
    return val1 if val11 > 21 else max(val1, val11)

#-------------------------------------------------------------------------------#
def player_wins(val1, val2):
#-------------------------------------------------------------------------------#
    print("hi_two_cons(20, 20): ", hi_two_cons(20, 20))
    print("hi_two_cons(27, 27): ", hi_two_cons(27, 27))

    # player_value? 
    player_value = hi_two_cons(20, 20)    
    # dealer_value? 
    dealer_value = hi_two_cons(27, 27)

    if (player_value > dealer_value):
        print("player wins")
    else:
        print("player dont win")


def test_pw(p1, p11, d1, d11):
    print(f"hi_two_cons({p1}, {p11}): ", hi_two_cons(p1, p11))
    print(f"hi_two_cons({d1}, {d11}): ", hi_two_cons(d1, d11))

    # player_value? 
    player_value = hi_two_cons(p1, p11)    
    # dealer_value? 
    dealer_value = hi_two_cons(d1, d11)

    if (player_value > dealer_value):
        print("player wins")
    else:
        print("player dont win")    

def test_hv(p1, p11, d1, d11):
    print("*--------------------------------------------------*")
    print(f"get_hand_val({p1}, {p11}): ", get_hand_val(p1, p11))
    print(f"get_hand_val({d1}, {d11}): ", get_hand_val(d1, d11))

    # hand_value? 
    player_value = get_hand_val(p1, p11)    
    # dealer_value? 
    dealer_value = get_hand_val(d1, d11)

    if (player_value > dealer_value):
        print("player wins")
    else:
        print("player dont win")    
print("htcons")
test_pw(23, 24, 27, 27)
test_pw(10, 11, 21, 22)
test_pw(11, 10, 22, 21)
test_pw(21, 22, 10, 11)
test_pw(22, 21, 11, 10)
test_pw(5, 6, 7, 8)
test_pw(7, 8, 5, 6)
test_pw(1, 23, 2, 24)
test_pw(23, 1, 24, 2)
test_pw(2, 23, 1, 24)
test_pw(23, 2, 24, 1)
test_pw(23, 25, 23, 25)

print("hv")
test_hv(20, 20, 27, 27)
test_hv(10, 11, 21, 22)
test_hv(11, 10, 22, 21)
test_hv(21, 22, 10, 11)
test_hv(22, 21, 11, 10)
test_hv(5, 6, 7, 8)
test_hv(7, 8, 5, 6)
test_hv(1, 23, 2, 24)
test_hv(23, 1, 24, 2)
test_hv(2, 23, 1, 24)
test_hv(23, 2, 24, 1)
test_hv(23, 25, 23, 25)

