#!/usr/bin/env python3
from brain_games.game_engine import engine
from brain_games.game.even_numbers import even


def main():
    engine(even, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    main()
