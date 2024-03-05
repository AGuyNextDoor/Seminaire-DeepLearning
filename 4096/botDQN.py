#!/usr/bin/env python3
from bothelper import read_board, up, down, left, right, botsetup, rotate_board, merge_count, print_board
from dqnlearner_bot import DQNLearner
import os
# register name
s = botsetup("smarter-example")

counter = 0

# dql_bot = DQLearner(...)

while True:
	board, score = read_board(s)

	best = 0
	best_dir = down
	best_score = 0
	dirs = [down, left, up, right]

	# Ecrire les étapes d'entrainement du bot ici
	# ...
