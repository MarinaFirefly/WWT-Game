#!/usr/bin/env python3
"""
ASCII scene for game help print
"""


def rules():
    '''Print ASCII scene.
    no params need
    ----------
    Returns jutp ASCII SCENE for Games rules
    -------
    '''
    print(r"""

                          _____                                     _           
                         / ____|                                   | |          
                        | |  __  __ _ _ __ ___   ___     _ __ _   _| | ___  ___ 
                        | | |_ |/ _` | '_ ` _ \ / _ \   | '__| | | | |/ _ \/ __|
                        | |__| | (_| | | | | | |  __/   | |  | |_| | |  __/\__ \
                         \_____|\__,_|_| |_| |_|\___|   |_|   \__,_|_|\___||___/
                                                                                
                                                                                
                Your turn is first.
                Choose you hero for attack and PC will choose its hero for defense randomly.
                If you defeat you enemy you will have +1 point. If enemy loose his life +5 points.
                After enemy loosed his life the level of the game increase (enemy has +1 live).
                You have 5 lives.

                Enemy has a next turn.
                If he defeats you loose one of your lives.

                Warrior defeats thief, thief defeats wizard, wizard defeats warrior.

                P.S. You can have more score but enemy is always wins 
""")
