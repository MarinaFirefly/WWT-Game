"""
Main Runner for WTT game
"""
import datetime
import sqlite3
from ascii_img.ask_user_name import ask_name
from ascii_img.credential import credential
from ascii_img.help import rules
from ascii_img.intro import intro
from scripts.models import Enemy
from scripts.models import Player


def play():
    """
    main function for game and write data to db
    """
    ask_name()
    player_name = input("   ")
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
        else:
            player.defence(enemy)
    save_to_db(player_name,player.score)

def save_to_db (name,score):
    """
    function saving to db
    """
    conn = sqlite3.connect("data/scores.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 
                scores (id serial, username text, score integer, dt text)""")
    cursor.execute("SELECT COUNT(*) FROM scores")
    new_id = cursor.fetchone()[0] + 1
    now = datetime.date.today()
    params = (new_id, name, score, now)
    cursor.execute("INSERT INTO scores VALUES (?,?,?,?)", params)
    conn.commit()
    conn.close()

def read_from_db():
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

if __name__ == '__main__':
    try:
        intro()
        first_input = input("    ").lower()
        if first_input == "start":
            play()
        elif first_input == "help":
            rules()
            new_game = input("WANT TO PLAY? (Y/N)   ")
            if new_game == "Y":
                play()
            elif new_game == "N":
                pass
        elif first_input == "about us":
            credential()
            new_game = input("WANT TO PLAY? (Y/N)   ")
            if new_game == "Y":
                play()
            elif new_game == "N":
                pass
        elif first_input == "exit":
            pass
        elif first_input == "score":
            try:
                read_from_db()
            except sqlite3.OperationalError:
                pass
            new_game = input("WANT TO PLAY? (Y/N)   ")
            if new_game == "Y":
                play()
            elif new_game == "N":
                pass
    except KeyboardInterrupt:
        print("Unacceptable character was entered!")
    except ValueError:
        print("Unacceptable character was entered!")
    finally:
        print("GOOD BYE!")
