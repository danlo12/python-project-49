#!/usr/bin/env python3
from brain_games.game_engine import run
from brain_games.games import calculate_game


def main():
    run(calculate_game)


if __name__ == '__main__':
    main()
