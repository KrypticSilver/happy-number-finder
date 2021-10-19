spacer = "=" * 63

def get_number():
    while True:
        print(spacer)
        print("What number do you want to check?")
        print(spacer)
        num = input(">>> ")

        try:
            num = int(num)
            return num

        except:
            print(spacer)
            print("Invalid input, please try again.")
            print(spacer)
            print("Do you want to exit to the main menu?")
            print("")
            print("1 = Exit to main menu.")
            print("2 = Try again.")


def is_happy(number):
    try:
        num_as_string = str(number)
        num_digits = len(num_as_string)

        total_value = 0

        if number == 1:
            return 1

        else:
            for i in range(num_digits):
                total_value += int(num_as_string[i]) ** 2

            return is_happy(total_value)
        

    except:
        return 0
            
def remain_question():
    while True:
        print(spacer)
        print("Do you want to check another number of quit?")
        print("")
        print("1 = Check another number.")
        print("2 = Quit.")
        print(spacer)
        check_again = input(">>> ")

        if check_again == "1":
            return True
        
        elif check_again == "2":
            return False

        else:
            print(spacer)
            print("Invalid input, please try again.")


while True:
    num = get_number()
    print(spacer)
    
    if is_happy(num):
        print(f"{num} is a happy number :)")

    else:
        print(f"{num} is not a happy number :(")

    if remain_question():
        continue
    
    else:
        break
