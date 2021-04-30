#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on April 2021
# This program calculates the sum of two numbers


def main():
    # this function calculates the sum

    # input
    print("Time to add up some numbers!")
    print("Follow the prompts down below:")
    print("")
    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))

    # process
    sum = number1 + number2

    # output
    print("")
    print("The sum of the numbers is {0} .".format(sum))


if __name__ == "__main__":
    main()
