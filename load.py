import sqlite3
from datetime import datetime
from logger import logger

def save_to_csv(df):
    filename = f"validated_users_{datetime.now().date()}.csv"
    df.to_csv(filename, index=False)
    logger.info(f"CSV saved: {filename}")

def load_to_sqlite(df):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            city TEXT,
            zipcode TEXT,
            phone_no TEXT,
            website TEXT,
            company_name TEXT
        )
    """)

    df.to_sql("users", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    logger.info("Data loaded into SQLite successfully")
