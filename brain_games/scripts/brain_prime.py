#!/usr/bin/env python3
from brain_games.game_engine import run_game
from brain_games.games.prime_game import prime


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(prime, rule)


if __name__ == '__main__':
    main()
