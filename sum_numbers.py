#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program shows the sum of all positive numbers from 0 to number entered


def main():
    # this program shows the sum of all positive numbers from 0 to number
    # entered
    counter = 0
    sum = 0

    # input
    positive_number = input("Enter any positive integer please: ")
    print("\n", end="")

    # process & output
    try:
        positive_number_int = int(positive_number)

        if positive_number_int > 0:
            while counter < positive_number_int:
                sum = sum + (counter+1)
                counter = counter + 1
            print("The sum of all positive numbers from 0 to {0} is {1}"
                  .format(positive_number_int, sum))

        else:
            print("That was not a positive integer. Enter an integer"
                  " above 0.")
            print("\n", end="")
    except Exception:
        print("That was not an integer. Please enter an integer.")


if __name__ == "__main__":
    main()
