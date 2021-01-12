#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program prints 10 random integers and finds the average

import random


def main():
    # input the number and decimal place

    # list
    random_list = []

    # process
    for loop_counter in range(0, 10):
        # random number
        random_number = random.randint(1, 100)
        random_list.append(random_number)
        print(random_number)

    average = (sum(random_list)) / 10

    print("")
    print("The average of these 10 numbers is: {0}".format(average))


if __name__ == "__main__":
    main()
