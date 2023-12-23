#!/usr/bin/env python3

import sys

def get_power(line: str) -> int:
    num_red = 12
    num_green = 13
    num_blue = 14
    digit_count = 0
    set_counts = {"r" : 0, "b": 0, "g": 0}
    counts_str = ""
    game_id = ""
    game_id_split = line.split(": ")
    semi_colon_split = game_id_split[1].split("; ")

    for game_set in semi_colon_split:
        for i, ch in enumerate(game_set):
            if ch.isdigit():
                counts_str += ch
            if ch == "b":
                if int(counts_str) > set_counts["b"]:
                    set_counts["b"] = int(counts_str)
                counts_str = ""
            if ch == "r" and game_set[i-1] == " ":
                if int(counts_str) > set_counts["r"]:
                    set_counts["r"] = int(counts_str)
                counts_str = ""
            if ch == "g":
                if int(counts_str) > set_counts["g"]:
                    set_counts["g"] = int(counts_str)
                counts_str = ""


    return set_counts["r"] * set_counts["g"] * set_counts["b"]

def sum_powers():
    sum = 0
    file = open('adventDay2_2023_input.txt', 'r')
    Lines = file.readlines()
    for line in Lines:
        sum += get_power(line)

    file.close()
    print(sum)


sum_powers()
