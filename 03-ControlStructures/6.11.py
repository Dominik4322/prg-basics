
 previous_price = 1
 current_price = int(input("Enter the current price of the item: "))
 procent = current_price / previous_price * 100
 procent_decrease = int(100 - procent)


if current_price < previous_price and procent_decrease >= 10:
    print("Buy the procuct now!")
    print(f"Price deacreased by {procent_decrease}%")




