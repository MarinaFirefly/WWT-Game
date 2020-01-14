"""
Main Runner for WTT game
"""
import datetime
import sqlite3
from ascii_img.ask_user_name import ask_name
from ascii_img.help import rules
from ascii_img.intro import intro
from scripts.models import Enemy
from scripts.models import Player
# from exceptions import EnemyDown


def play():

    ask_name()
    player_name = input("           ")
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
<<<<<<< HEAD
    cursor.execute("CREATE TABLE IF NOT EXISTS scores (id serial, username text, score integer, dt text)")
=======
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS scores (id serial, username text, score text, dt text)")
>>>>>>> 08d62afa508e952c1c981b5fa7b87cff124e9ed9
    cursor.execute("SELECT COUNT(*) FROM scores")
    new_id = cursor.fetchone()[0] + 1
    now = datetime.date.today()
    params = (new_id, player_name, int(player.score), now)
    cursor.execute("INSERT INTO scores VALUES (?,?,?,?)", params)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    try:
        intro()
        first_input = input("    ")
        if first_input.lower() == "start":
            play()
        elif first_input.lower() == "help":
            rules()
            new_game = input("WANT TO PLAY? (Y/N)   ")
            if new_game == "Y":
                play()
            elif new_game == "N":
                pass
        elif first_input.lower() == "exit":
            pass
        elif first_input.lower() == "score":
            try:
                conn = sqlite3.connect("data/scores.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 10")
                scores_result = cursor.fetchall()
                if scores_result != []:
                    for result in scores_result:
                        print(f"{result[1]}     |   {result[3]}   |   {result[2]}")
                else:
                    print("NO RESULTS IN DB!")
                conn.close()
            except sqlite3.OperationalError:
                pass
            new_game = input("WANT TO PLAY? (Y/N)   ")
            if new_game == "Y":
                play()
            elif new_game == "N":
                pass
    except KeyboardInterrupt:
        print("Unacceptable character was entered!")
        pass
    except ValueError:
        print("Unacceptable character was entered!")
        pass
    finally:
        print("Good bye!")

