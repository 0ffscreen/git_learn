from gamble import run
from roulette import spin_roulette
print("welcome to the empire's greatest casino! You can play the game and try to win some nothing! Good luck!")
game_choice = input("press 1 for black jack, 2 for roulette, 3 for slots, or 4 to exit: ")
if game_choice == "1":
    print("You have chosen to play blackjack!")
    while True:
        run()
        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break
if game_choice == "2":
    print("You have chosen to play roulette!")
    while True:
        bet = input("enter a number or colour to bet on: ")
        spin_result = spin_roulette()
        print(f"The roulette wheel landed on: {spin_result}")
        if bet in ["red", "black"]:
            if (bet == "red" and spin_result in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]) or (bet == "black" and spin_result in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]):
                print("You win!")
            elif (bet == 0 and spin_result == 0):
                print("You win the jackpot!")
            elif bet.isdigit() and int(bet) == spin_result:
                print("You win jackpot!")
            else:
                print("You lose!")
        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break
                