import bcrypt
from database import connect_db

def create_user(username, password, role="admin"):
    conn = connect_db()
    cursor = conn.cursor()

    # Hash the password
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert username, password hash, and role
    query = "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, hashed, role))

    conn.commit()
    conn.close()


# Create an admin user
create_user("admin3", "admin_123")