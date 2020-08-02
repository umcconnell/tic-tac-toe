"""CLI AI Selector"""
from src.ai import ABPrunedMinimaxPlayer, MinimaxPlayer, RandomPlayer

from .cli import ARGS

ai_type = ARGS.ai
mm_depth = ARGS.depth

#: User specified AI
AI = None
if ai_type == 'random':
    AI = RandomPlayer()
elif ai_type == 'minimax':
    AI = MinimaxPlayer(mm_depth)
elif ai_type == 'abprune_minimax':
    AI = ABPrunedMinimaxPlayer(mm_depth)

if AI:
    print('Chosen Computer Opponent is %s' % type(AI).__name__)
else:
    print('Multiplayer Mode!')
    print()
    print('NOTE:')
    print("Run with '--ai minimax' to play against unbeatable computer")
    print("Use -h to see other available options")

print()
