#!/usr/bin/env python3
from brain_games.game.game_engine import engine
from brain_games.game.even_numbers import quest
from brain_games.game.cli import welcome_user

def main():
    print('Welcome to the Brain Games!')
    engine(1, 'Answer "yes" if the number is even, otherwise answer "no".')

if __name__ == '__main__':
    main()

