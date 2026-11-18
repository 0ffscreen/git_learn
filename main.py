
from dealer import dealer


def main():
    print("Welcome to the Empire's greatest casino!")
    print("Dealer: What would you like to play?")

    while True:
        user_input = input("\nYou: ")

        response = dealer(user_input)

        if response == "exit":
            print("Dealer: Goodbye! Come back soon.")
            break

        print(response)


if __name__ == "__main__":
    main()
