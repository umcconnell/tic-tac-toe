"""Main module"""
from src.game import Game
from src.cli import AI

if __name__ == "__main__":
    game = Game(ai=AI)
    game.start()
