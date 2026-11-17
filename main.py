from gamble import run
print("Well hello there!")
while True:
    run()
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        print("Thanks for playing! Goodbye!")
        break