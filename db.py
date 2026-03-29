import sqlite3
from datetime import datetime
import logging

from config import DATABASE_NAME

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init_db():
    """Initializes the SQLite database and creates the messages table if it doesn't exist."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                username TEXT,
                text TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        logging.info(f"Database '{DATABASE_NAME}' initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error initializing database: {e}")

def insert_message(user_id: int, username: str, message_text: str):
    """Inserts a new message into the database."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        timestamp = datetime.now().isoformat()
        cursor.execute("INSERT INTO messages (user_id, username, text, timestamp) VALUES (?, ?, ?, ?)",
                       (user_id, username, message_text, timestamp))
        conn.commit()
        conn.close()
        logging.info(f"Message from user_id {user_id} saved to database.")
        return True
    except sqlite3.Error as e:
        logging.error(f"Error inserting message into database: {e}")
        return False
