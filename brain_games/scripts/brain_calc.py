#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games.calculate_game import calc


def main():
    run_game(calc, 'What is the result of the expression?')


if __name__ == '__main__':
    main()
