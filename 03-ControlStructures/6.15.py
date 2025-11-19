number = int(input("Enter EAN Article Number: "))
number = str(number)
number_lenght = len(str(number))

def check_product():
    if number.startswith('590'):
        print("The product is from Poland.")
    else:
        print("The product is not from Poland.")
    

if number_lenght == 13:
    print("The EAN Article Number is correct.")
    check_product()
elif number_lenght < 13 or number_lenght > 13:
    print("The EAN Article Number is incorrect.")
    check_product()

