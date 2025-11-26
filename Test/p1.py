
def f(amout_to_pay):
    coins = [1,2,5]
    count = 0

    for i in coins:
        count += amout_to_pay // i
        amout_to_pay %= i
    return count




