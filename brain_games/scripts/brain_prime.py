#!/usr/bin/env python3
from brain_games.game.game_engine import engine
from brain_games.game.prime_game import prime


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine(prime, rule)


if __name__ == '__main__':
    main()
