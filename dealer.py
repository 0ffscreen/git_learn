
from games import blackjack_game, roulette_game
from ai_client import ask_dealer


# Available casino games
TOOLS = {
    "blackjack": {
        "description": "Play blackjack at the Diamond Casino",
        "keywords": ["blackjack", "black jack"],
        "call": blackjack_game
    },

    "roulette": {
        "description": "Try your luck at the Diamond Casino roulette table",
        "keywords": ["roulette"],
        "call": roulette_game
    }
}


def dealer(user_input):
    """Vincent - Senior Dealer at the Diamond Casino & Resort."""

    message = user_input.lower().strip()

    if message in ["exit", "quit", "bye", "leave"]:
        return "exit"

    response = ask_dealer(user_input, mock=True)

    tool_name = response.get("tool")
    content = response.get("content", "")

    if tool_name in TOOLS:
        print(f"\nVincent: {content}")
        print("Vincent: Right this way, please...\n")

        TOOLS[tool_name]["call"]()

        return "Vincent: Back already? The house appreciates your business."

    return f"Vincent: {content}"
