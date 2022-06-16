class TooLongNumber(Exception):
    pass


while True:
    print("What do you want to do?\n 1-sum\n 2-subtract\n 3-multipy\n 4-divide\n 5-exit")
    user_choice = int(input("your choice: "))
    if user_choice < 5:
        try:
            first_number = int(input("first number: "))
            second_number = int(input("second number: "))
            if user_choice == 1:
                print(first_number + second_number)
            elif user_choice == 2:
                print(first_number - second_number)
            elif user_choice == 3:
                print(first_number * second_number)
            elif user_choice == 4:
                try:
                    print(first_number / second_number)
                except ZeroDivisionError:
                    print("I can't divide into 0")
            else:
                print("Choose right variant")
                print(user_choice)
        except ValueError:
            print("Enter number")
    elif user_choice == 5:
        break
    else:
        raise TooLongNumber
