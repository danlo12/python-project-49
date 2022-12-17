#!/usr/bin/env python3
from brain_games.game.game_engine import engine


def main():
    print('Welcome to the Brain Games!')
    engine(5, 'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == '__main__':
    main()
