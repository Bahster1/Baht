import sqlite3
from sqlite3 import Error


PURPLE = '\033[95m'
CYAN = '\033[96m'
DARK_CYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'


def connect_to_database():
    con = None

    try:
        con = sqlite3.connect("data.db")
    except Error as e:
        print(e)

    return con


def initialize_database():
    con = connect_to_database()
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS users( 
    user_id INTEGER,
    guild INTEGER, 
    social_credit INTEGER,
    UNIQUE(user_id, guild))''')

    con.close()


def is_user_present(user_id, guild_id):
    """
    Checks the users table for the specified user_id.
    """
    con = connect_to_database()
    cur = con.cursor()
    result = cur.execute(f'''SELECT * FROM users WHERE user_id={user_id} AND guild={guild_id}''').fetchall()

    cur.close()
    con.close()

    return not result == []


def get_social_credit(user_id, guild_id):
    """
    Retrieve a specified user's social credit.

    :param user_id: integer
    :param guild_id: integer
    """
    con = connect_to_database()
    cur = con.cursor()

    if not is_user_present(user_id, guild_id):
        add_user(user_id, guild_id)

    sc = cur.execute(f'''SELECT social_credit FROM users WHERE user_id={user_id} AND guild={guild_id}''').fetchone()[0]

    cur.close()
    con.close()

    return sc


def add_user(user_id, guild_id):
    """
    Add a new user to the table.
    social_credit will default to 0.

    :param user_id: integer
    :param guild_id: integer
    """
    con = connect_to_database()
    cur = con.cursor()

    cur.execute(f'''INSERT INTO users VALUES ({user_id}, {guild_id}, 0)''')
    con.commit()
    cur.close()
    con.close()


def set_social_credit(user_id, guild_id, social_credit):
    """
    Add user to table if they are not present.
    Set a specified user's social credit.

    :param user_id: integer
    :param guild_id: integer
    :param social_credit: integer
    """
    con = connect_to_database()
    cur = con.cursor()

    if not is_user_present(user_id, guild_id):
        add_user(user_id, guild_id)

    cur.execute(f'''UPDATE users SET social_credit={social_credit} WHERE user_id={user_id} AND guild={guild_id}''')

    con.commit()
    cur.close()
    con.close()


def add_social_credit(user_id, guild_id, social_credit):
    """
    Add user to table if they are not present.
    Modify a specified user's social_credit.

    :param user_id: integer
    :param guild_id: integer
    :param social_credit: integer
    """
    con = connect_to_database()
    cur = con.cursor()

    if not is_user_present(user_id, guild_id):
        add_user(user_id, guild_id)

    current_sc = get_social_credit(user_id, guild_id)

    current_sc += social_credit
    cur.execute(f'''UPDATE users SET social_credit={current_sc} WHERE user_id={user_id} AND guild={guild_id}''')

    con.commit()
    cur.close()
    con.close()
