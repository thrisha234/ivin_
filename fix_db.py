import sqlite3

DB_PATH = r"C:\Users\thrisha\Downloads\board_meeting_ai_4sp_v2\db\meetings.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(attendance)")
existing_cols = [col[1] for col in cursor.fetchall()]

if "first_seen" not in existing_cols:
    cursor.execute("ALTER TABLE attendance ADD COLUMN first_seen TEXT")

if "last_seen" not in existing_cols:
    cursor.execute("ALTER TABLE attendance ADD COLUMN last_seen TEXT")

conn.commit()
conn.close()

print("✅ Database fixed successfully!")
