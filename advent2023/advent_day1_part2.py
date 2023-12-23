#!/usr/bin/env python3

import sys

def get_calibration_value(line: str) -> int:
    value = ""
    digits = { "one" : "1", "two" : "2", "three" :  "3",
              "four" : "4", "five" : "5", "six" : "6",
              "seven" : "7", "eight" : "8", "nine" : "9"}
    reversed_digits = { "eno" : "1", "owt" : "2", "eerht" : "3",
                       "ruof" : "4", "evif" : "5", "xis" : "6",
                       "neves" : "7", "thgie" : "8", "enin" : "9"}
    min_index = sys.maxsize
    min_reversed_index = sys.maxsize
    num_index = -1
    num_reversed_index = -1
    min_str = ""
    max_str = ""
    reversed_line = line[::-1]

    for num in [*digits,  *digits.values()]:
        num_index = line.find(num)

        if num_index == -1:
            continue

        if num_index < min_index:
            min_index = num_index
            min_str = num

    for num in [*reversed_digits, *reversed_digits.values()]:
        num_reversed_index = reversed_line.find(num)

        if num_reversed_index == -1:
            continue

        if num_reversed_index < min_reversed_index:
            min_reversed_index = num_reversed_index
            max_str = num



    if min_str.isdigit():
        value += min_str
    else:
        value += digits[min_str]

    if max_str.isdigit():
        value += max_str
    else:
        value += reversed_digits[max_str]



    return int(value)

def sum_calibration_values():
    sum = 0
    file = open('adventDay1_2023_input.txt', 'r')
    Lines = file.readlines()
    for line in Lines:
        sum += get_calibration_value(line)

    file.close()
    print(sum)


sum_calibration_values()
