#!/usr/bin/env python3

# Created by: Lucas LeBlanc
# Created on: Dec 2022
# This program finds the average of random numbers

import random


def average_of_numbers(rows, columns, passed_list):
    # This function gets the average

    total = 0
    for row_value in passed_list:
        for element in row_value:
            total += element
    total = total / (rows * columns)

    return total


def main():
    # This function uses the list

    row_number_list = []

    rows = input("How many rows would you like: ")
    columns = input("How many columns would you like: ")

    try:
        rows_integer = int(rows)
        columns_integer = int(columns)

        for counter_rows in range(0, rows_integer):
            temp_column = []
            for counter_columns in range(0, columns_integer):
                random_number = random.randint(0, 50)
                temp_column.append(random_number)
                print("{0} ".format(random_number), end="")
            row_number_list.append(temp_column)
            print("")

        average = average_of_numbers(rows_integer, columns_integer, row_number_list)
        print("\nThe average of the numbers is: {0}".format(average))
    except Exception:
        print("\nInvalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
