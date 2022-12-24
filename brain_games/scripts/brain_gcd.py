#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games.gcd_game import gcd_g


def main():
    run_game(gcd_g, "Find the greatest common divisor of given numbers.")


if __name__ == '__main__':
    main()
