import bcrypt
from database import connect_db


def login(username, password):

    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT password_hash FROM users WHERE username=%s"
    cursor.execute(query, (username,))

    row = cursor.fetchone()

    conn.close()

    if row:

        stored_hash = row[0]

        # ensure hash is bytes
        if isinstance(stored_hash, str):
            stored_hash = stored_hash.encode('utf-8')

        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            return True

    return False