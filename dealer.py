
from games import blackjack_game, roulette_game


# Available tools
TOOLS = {
    "blackjack": {
        "description": "Play a game of blackjack",
        "keywords": ["blackjack", "black jack"],
        "call": blackjack_game
    },

    "roulette": {
        "description": "Play roulette",
        "keywords": ["roulette"],
        "call": roulette_game
    }
}


def dealer(user_input):
    """Interpret user input and execute matching tools."""

    message = user_input.lower().strip()

    if message in ["exit", "quit", "bye"]:
        return "exit"

    if message in ["help", "games", "menu"]:
        return "Available games: " + ", ".join(TOOLS)

    for name, tool in TOOLS.items():
        if any(word in message for word in tool["keywords"]):
            print(f"Dealer: Excellent choice! Let's play {name}.")
            tool["call"]()
            return f"Dealer: Welcome back from {name}!"

    return "Dealer: I didn't understand. Type 'help' for games."
