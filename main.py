"""This module checks the efficiency of the user's password."""

import string
import urwid


def is_very_long(password):

    return len(password) > 12


def has_digit(password):

    return any(element.isdigit() for element in password)


def has_letters(password):

    return any(element.isalpha() for element in password)


def has_upper_letters(password):

    return any(element.isupper() for element in password)


def has_lower_letters(password):

    return any(element.islower() for element in password)


def has_symbols(password):

    return any(element in string.punctuation or element == ' ' for element in password)


def score(password):
    """Calculate the password strength score based on various criteria."""
    score = 0
    list_of_params = {
        'length': is_very_long,
        'digit': has_digit,
        'letters': has_letters,
        'upper_letter': has_upper_letters,
        'lower_letters': has_lower_letters,
        'symbols': has_symbols,
    }
    for param_name, param_func in list_of_params.items():
        if param_func(password):
            score += 2
    return score


def on_ask_change(edit, new_edit_text):

    password_score = score(new_edit_text)

    reply.set_text(f"Рейтинг пароля: {password_score}")

def main():
    ask = urwid.Edit('Введите пароль: ', mask='*')
    global reply 
    reply = urwid.Text("Рейтинг пароля: 0")  
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    
    
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
if __name__=="__main__":
    main()
