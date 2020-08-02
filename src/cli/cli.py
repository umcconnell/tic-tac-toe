"""Tic-Tac-Toe CLI Configuration"""
import argparse

#: Argparse argument parser
PARSER = argparse.ArgumentParser(
    description='Play tic-tac-toe against an unbeatable machine!')
PARSER.add_argument('--ai', type=str, default='none',
                    choices=['none', 'random', 'minimax', 'abprune_minimax'])
PARSER.add_argument('--depth', type=int, default=None,
                    help='Maximum depth in the minimax algorithm')
ARGS = PARSER.parse_args()

print("=================\n ★ tic-tac-toe ★ \n=================")
