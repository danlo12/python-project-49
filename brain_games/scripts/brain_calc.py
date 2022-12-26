#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games import calculate_game


def main():
    run_game(calculate_game)


if __name__ == '__main__':
    main()
