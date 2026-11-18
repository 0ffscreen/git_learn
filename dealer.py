
from games import blackjack_game, roulette_game
from dealer_prompt import DEALER_INSTRUCTIONS

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



from ai_client import ask_dealer


def dealer(user_input):
    message = user_input.lower().strip()

    if message in ["exit", "quit", "bye"]:
        return "exit"

    response = ask_dealer(user_input, mock=True)

    tool_name = response.get("tool")
    content = response.get("content", "")

    if tool_name in TOOLS:
        TOOLS[tool_name]["call"]()

    return f"Dealer: {content}"
