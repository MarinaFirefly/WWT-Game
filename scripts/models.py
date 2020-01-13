import random
#from exceptions import EnemyDown
#from exceptions import GameOver


class Enemy:
    def __init__(self, level):
        self.level = level

    @staticmethod
    def select_attack():
        return random.choice([1,2,3])

    def decrease_lives(self):
        self.level -= 1
        if self.level == 0:
            #raise EnemyDown()
            print("Enemy Down!")
        return self.level


class Player:
    def __init__(self, name, lives=5, score=0):#, allowed_attacks):
        self.name = name
        self.lives = lives
        self.score = score
#        self.allowed_attacks = allowed_attacks

    @staticmethod
    def fight(attack, defense):
        res = None
        if attack == defense:
            res = 0
        elif (attack == 1 and defense == 2) or (attack == 2 and defense == 3) or (attack == 3 and defense == 1):
            res = 1
        elif (attack == 2 and defense == 1) or (attack == 3 and defense == 2) or (attack == 1 and defense == 3):
            res = -1
        return res

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
           # raise GameOver
            print ("You loosed last live! Game over!")
        return self.lives

    def choose_hero(self):
        return int(input("Choose your hero"))

#    @staticmethod
    def attack(self, enemy_obj):
        enemy_attack = enemy_obj.select_attack()
        player_attack = self.choose_hero()
        fight_result = self.fight(player_attack,enemy_attack)
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
        enemy_attack = enemy_obj.select_attack()
        player_attack = self.choose_hero()
        fight_result = self.fight(enemy_attack,player_attack)
        if fight_result == 0:
            print("It's a draw!")
        elif fight_result == 1:
            print("Enemy's attack was succsessfull! And you loosed one of lives!")
            self.decrease_lives()
        elif fight_result == -1:
            print("Your enemy missed!")
