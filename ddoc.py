import random
def draw_value():
    card=random.randint(1, 13)
    if card==1:
        return 11   
    elif card>10:
        return 10      
    else:
        return card 


