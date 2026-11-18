
import json
from config import MODEL_NAME, MODEL_BASE_URL, MODEL_API_KEY
from dealer_prompt import DEALER_INSTRUCTIONS


def ask_dealer(user_input, mock=True):
    """Send a player message to the casino AI dealer."""

    if mock:
        message = user_input.lower()

        if "roulette" in message:
            tool = "roulette"
        elif "blackjack" in message or "black jack" in message:
            tool = "blackjack"
        else:
            tool = None

        return {
            "content": "Welcome to the casino! Feeling lucky?",
            "tool": tool
        }

    # Future OpenAI-compatible API integration
    from openai import OpenAI

    client = OpenAI(
        api_key=MODEL_API_KEY,
        base_url=MODEL_BASE_URL
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": DEALER_INSTRUCTIONS},
            {"role": "user", "content": user_input}
        ]
    )

    return json.loads(response.choices[0].message.content)
