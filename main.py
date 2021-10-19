spacer = "=" * 63


def get_range():
    while True:
        print(spacer)
        print("What is the range of happy numbers from 0 that you want to find? ")
        print(spacer)
        range = input(">>> ")

        try:
            range = int(range)
            return range

        except:
            print("Invalid input, please try again.")
            print(spacer)
            print("Do you want to exit to the main menu?")
            print("1 = Exit to main menu.")
            print("2 = Try again.")


def is_happy(number):
    iterations = 0

    while (number != 0) and (iterations < 1000):
        pass


is_happy(20)
