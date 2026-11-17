from ddoc import draw_value

def run():
    dealer = 0
    previous_score = 0
    dealer += draw_value()
    while dealer <= 21:
        previous_score = dealer
        print("Dealer's total:", dealer)
        dealer += draw_value()
    dealer = previous_score
    print("Dealer's final total:", dealer)
    player = draw_value()
    user_input = "hit"
    print("Player's total:", player)
    while player < 21 and user_input == "hit":
        user_input = input("Do you want to hit or stay? ")
        if user_input == "hit":
            player += draw_value()
            print("Player's total:", player)
    if player > 21:
        print("Player busts! Dealer wins.")
    elif player < dealer:
        print("Dealer wins!")
    elif player > dealer:
        print("Player wins!")
    else:
        print("It's a tie!")