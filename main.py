def deposit():
    while True:
        amount = input("enter ammount to deposit")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("amount must be greater than 0")

        else:
            print("enter a number")

    return amount

def get_number_of_lines():
    


deposit()

def main():
    balance = deposit()

main()
    