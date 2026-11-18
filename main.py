
from dealer import dealer


def main():
    print("=" * 60)
    print("         THE DIAMOND CASINO & RESORT")
    print("                 LOS SANTOS")
    print("=" * 60)

    print("\nVincent: Welcome to the Diamond.")
    print("Vincent: Where dreams are made...")
    print("Vincent: ...and bank accounts are emptied.")

    print("\nAvailable games: Blackjack | Roulette")
    print("Type 'exit' to leave.\n")

    while True:
        user_input = input("Guest: ")

        response = dealer(user_input)

        if response == "exit":
            print("\nVincent: Leaving already?")
            print("Vincent: Come back when you've made more money.")
            break

        print(response)


if __name__ == "__main__":
    main()
