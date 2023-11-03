def check_digit():
    while True:
        num = input("Enter your number: ")
        try:
            num = int(num)
            if 0 < num < 100:
                print(num)
                return
            else:
                print("enter a number in the range 0 to 100")
        except ValueError:
            print("this is not a number!!! Try again.")


check_digit()
