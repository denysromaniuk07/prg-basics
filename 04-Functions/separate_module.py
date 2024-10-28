def separate(number, x,y):
    if number >x and number <y:
        return True
    else:
        return False
    
def hide(card_number):
    masked = card_number[:2] + '*' * 10 + card_number[-4:]
    return masked