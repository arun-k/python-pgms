
def count_change(amnt,coins):
    if amnt==0:
        return 1
    elif amnt < 0:
        return 0
    elif amnt > 0 and len(coins) <= 0:
        return 0
    else:
        return count_change(amnt-coins[0],coins) + count_change(amnt,coins[1:])
