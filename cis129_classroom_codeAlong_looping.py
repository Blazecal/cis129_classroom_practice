# Calvin Barnett (gamer)
# March 11 2024


def main():
    while True:
        user_number = get_integer("Enter a number: ")
    
        if (user_number % 2 == 0):
            print("The number is even!")
        else:
            print("The number is odd!")
        print("Do you want to do it again?")
        again = input("Enter \"y\" to loop again: ")
        if again.lower() != 'y':
            break
    print("The loop has ended")

# Input Function     
def get_integer(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print ("Incorrect data entered, please re-attempt")

main()
