# def new_balance(old_balance, withdrawn_amount):
#     return old_balance - withdrawn_amount

def withdraw_cash(pin_number, cash_withdrawn):
    saved_pin_number = 1234
    current_balance = 4450
    if pin_number != saved_pin_number:
        print('Password Error')
    elif cash_withdrawn > current_balance:
        print('Insufficient Funds')
    else:
        print('Dispensing cash')
        current_balance = current_balance - cash_withdrawn
        # current_balance = new_balance(current_balance,cash_withdrawn)
        print('Your new balance is {}'.format(current_balance))

withdraw_cash(1234,200)