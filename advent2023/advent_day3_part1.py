#!/usr/bin/env python3
def symbol_nearby(x_coord, y_coord, x_max, y_max, symbol_coords) -> bool:
    for i in range(max(0, y_coord - 1), min(y_max, y_coord + 2)):
        for j in range(max(0,x_coord - 1), min(x_max, x_coord + 2)):
            if (j, i) in symbol_coords:
                return True

    return False

def sum_part_numbers():
    total = 0
    file = open('advent_Day3_test.txt', 'r')
    symbol_coords = set()
    lines = file.readlines()
    y_max = len(lines)
    x_max = len(lines[0])
    num = 0
    is_part_number = False
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if (not ch.isdigit()) and ch != ".":
                symbol_coords.add((j, i))

    for i, line in enumerate(lines): # down rows
        for j, ch in enumerate(line): # down columns
            if ch.isdigit():
                num = num * 10 + int(ch)
                if not is_part_number:
                    is_part_number = symbol_nearby(j, i, x_max, y_max, symbol_coords)

            if is_part_number and ((not ch.isdigit()) or (j == x_max - 1)):
                print(num)
                total += num
                is_part_number = False
                num = 0

            if (not ch.isdigit()) and (not is_part_number):
                num = 0



 

    file.close()
    print(f'The number is {total}')

sum_part_numbers()
