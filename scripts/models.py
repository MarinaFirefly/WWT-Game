"""
Behavior of our game work
"""
import random

from ascii_img.choice_of_hero import choice_of_hero
from ascii_img.game_end import game_over
from ascii_img.thief_win import thief_win
from ascii_img.warrior_win import warrior_win
from ascii_img.wizard_win import wizard_win
#from exceptions import EnemyDown
#from exceptions import GameOver


class Enemy:
    def __init__(self, level):
        self.level = level

    @staticmethod
    def select_attack():
        return random.choice([1, 2, 3])

    def decrease_lives(self):
        self.level -= 1
        if self.level == 0:
            #raise EnemyDown()
            print("Enemy Down!")
        return self.level


class Player:
    def __init__(self, name, lives=5, score=0):  # , allowed_attacks):
        self.name = name
        self.lives = lives
        self.score = score
#        self.allowed_attacks = allowed_attacks

    @staticmethod
    def fight(attack, defense):
        res = None
        if attack == defense:
            res = 0
        elif attack == 2 and defense == 1:
            #print("Wizard wins!")
            wizard_win()
            res = 1
        elif attack == 3 and defense == 2:
            #print("Thief wins!")
            thief_win()
            res = 1
        elif attack == 1 and defense == 3:
            #print("Warrior wins!")
            warrior_win()
            res = 1
        elif attack == 1 and defense == 2:
            #print("Wizard wins!")
            wizard_win()
            res = -1
        elif attack == 2 and defense == 3:
            #print("Thief wins!")
            thief_win()
            res = -1
        elif attack == 3 and defense == 1:
            #print("Warrior wins!")
            warrior_win()
            res = -1
        return res

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
           # raise GameOver
            #print ("You loosed last live! Game over!")
            game_over()
        return self.lives

    def choose_hero(self):
        return int(input('    '))

#    @staticmethod
    def attack(self, enemy_obj):
        print("Your turn!")
        enemy_attack = enemy_obj.select_attack()
        choice_of_hero()
        player_attack = self.choose_hero()
        fight_result = self.fight(player_attack, enemy_attack)
        if fight_result == 0:
            print("It's a draw!")
        elif fight_result == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            self.score += 1
        elif fight_result == -1:
            print("You missed!")
        else:
            print('User entered wrong data!')

#    @staticmethod
    def defence(self, enemy_obj):
        print("Enemy turn!")
        enemy_attack = enemy_obj.select_attack()
        choice_of_hero()
        player_attack = self.choose_hero()
        fight_result = self.fight(enemy_attack, player_attack)
        if fight_result == 0:
            print("It's a draw!")
        elif fight_result == 1:
            print("Enemy's attack was succsessfull! And you loosed one of lives!")
            self.decrease_lives()
        elif fight_result == -1:
            print("Your enemy missed!")
