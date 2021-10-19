spacer = "=" * 60


def get_range():
    while True:
        print(spacer)
        print("What is the range of happy numbers from 0 you want to find? ")
        print(spacer)
        range = input(">>> ")
        try:
            range = int(range)
            return range
        
        except:
            print("Invalid input, please try again.")

def is_happy(number):
    iterations = 0

    while (number != 0) and (iterations < 1000):
        



