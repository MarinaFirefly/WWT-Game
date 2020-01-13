import datetime
import sqlite3
from ascii_img.ask_user_name import ask_name
from ascii_img.intro import intro
from scripts.models import Enemy
from scripts.models import Player
#from exceptions import EnemyDown


def play():
    ask_name()
    player_name = input("")
    player = Player(player_name)
    level = 1
    enemy = Enemy(level)
    while player.lives > 0:
        player.attack(enemy)
        if enemy.level == 0:
            level += 1
            enemy = Enemy(level)
            player.score += 5
        print(f"Your score is {player.score}")
        player.defence(enemy)
        print(player.score)
    conn = sqlite3.connect("data/scores.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scores (id serial, username text, score text, dt text)")
    cursor.execute("SELECT COUNT(*) FROM scores")
    new_id = cursor.fetchone()[0] + 1
    now = datetime.datetime.today()
    params = (new_id, player_name, player.score, now)
    cursor.execute("INSERT INTO scores VALUES (?,?,?,?)",params)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    try:
        intro()
        first_input = input()
        if first_input == "start":
            play()
    except KeyboardInterrupt:
        print("Unacceptable character was entered!")
        pass
    except ValueError:
        print("Unacceptable character was entered!")
        pass
    finally: 
        print("Good bye!")
