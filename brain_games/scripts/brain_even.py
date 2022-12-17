#!/usr/bin/env python3
from brain_games.game.game_engine import engine


def main():
    print('Welcome to the Brain Games!')
    engine(1, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    main()
