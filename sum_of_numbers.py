#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sept 2019
# Modified by: Titwech Wal
# Modified on: Apirl 22, 2021
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number.


def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    # get the user number as a string
    user_number_string = input("Enter a positive number: ")
    print("")

    try:
        # convert to string
        user_number = int(user_number_string)

        if user_number >= 0:
            while (loop_counter <= user_number):
                sum = sum + loop_counter
                print("Tracking {0} times through loop.".format(loop_counter))
                loop_counter = loop_counter + 1

            print("")
            print("The sum of the numbers from 0 to {} is: {}."
                  .format(user_number, sum))
        else:
            print('You entered a negitive number, try again')

    except Exception:
        print("{} is not a valid number.". format(user_number_string))


if __name__ == "__main__":
    main()
