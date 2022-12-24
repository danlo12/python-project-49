#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games.even_game import even


def main():
    run_game(even, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    main()
