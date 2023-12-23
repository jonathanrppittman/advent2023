#!/usr/bin/env python3

import sys

def get_possible_game_id(line: str) -> int:
    num_red = 12
    num_green = 13
    num_blue = 14
    digit_count = 0
    set_counts = {"r" : 0, "b": 0, "g": 0}
    counts_str = ""
    game_id = ""
    game_id_split = line.split(": ")
    semi_colon_split = game_id_split[1].split("; ")
    for character in game_id_split[0]: #gets game id
        if character.isdigit():
            game_id += character

    for game_set in semi_colon_split:
        for i, ch in enumerate(game_set):
            if ch.isdigit():
                counts_str += ch
            if ch == "b":
                set_counts["b"] = int(counts_str)
                counts_str = ""
            if ch == "r" and game_set[i-1] == " ":
                set_counts["r"] = int(counts_str)
                counts_str = ""
            if ch == "g":
                set_counts["g"] = int(counts_str)
                counts_str = ""

        if num_red - set_counts["r"] < 0:
            return 0
        if num_green - set_counts["g"] < 0:
            return 0
        if num_blue - set_counts["b"] < 0:
            return 0

    return int(game_id) 

def sum_game_ids():
    sum = 0
    file = open('adventDay2_2023_input.txt', 'r')
    Lines = file.readlines()
    for line in Lines:
        sum += get_possible_game_id(line)

    file.close()
    print(sum)


sum_game_ids()
