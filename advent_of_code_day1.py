# Advent of Code 2021 Day 1
import pygame.event

with open("./data/input-day1.txt") as f:
    depths = []

    for line in f:
        depths.append(int(line))

print(depths)

