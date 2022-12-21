#!/usr/bin/env python3
from brain_games.game.game_engine import engine
from brain_games.game.gcd_game import gcd_g


def main():
    engine(gcd_g, "Find the greatest common divisor of given numbers.")


if __name__ == '__main__':
    main()
