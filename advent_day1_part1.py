#!/usr/bin/env python3

def get_calibration_value(line: str) -> int:
    value = ""
    for element in line:
        if element.isdigit():
            value += element
            break
    for element in reversed(line):
        if element.isdigit():
            value += element
            break

    return int(value)

def sum_calibration_values():
    sum = 0
    file = open('adventDay1_2023_input.txt', 'r')
    Lines = file.readlines()
    for line in Lines:
        sum += get_calibration_value(line)
    
    print(sum)


sum_calibration_values()
