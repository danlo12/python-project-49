#!/usr/bin/env python3
from brain_games.game_engine import engine
from brain_games.game.calculate_game import calc


def main():
    engine(calc, 'What is the result of the expression?')


if __name__ == '__main__':
    main()
