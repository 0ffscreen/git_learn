import random
def spin_roulette():
    roulettes = [i for i in range(37)]  # Numbers 0-36
    spin_result = random.choice(roulettes) 
    return spin_result