"""
Try catch exceptions
"""


class EnemyDown(Exception):
    '''Try catch exceptions for GAME Down case
    no params need
    ----------
    Rise jutt exceptions
    -------
    '''
    # pass  # If left just pass pylint unhappy with Unnecessary pass statement (unnecessary-pass)
    print("Enemy Down!")


class GameOver(Exception):
    '''Try catch exceptions for GAME over case
    no params need
    ----------
    Rise jutt exceptions
    -------
    '''
    # pass # If left just pass pylint unhappy with Unnecessary pass statement (unnecessary-pass)
    print("Game over!")
