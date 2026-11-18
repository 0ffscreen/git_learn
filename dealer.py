def dealer(user_input):
    command = user_input.lower()

    if "blackjack" in command:
        return play_blackjack()

    elif "roulette" in command:
        return play_roulette()

    else:
        return "Welcome! Would you like blackjack or roulette?"