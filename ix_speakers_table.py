import sqlite3

DB_PATH = "db/meetings.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Add the missing 'embedding' column
cursor.execute("""
ALTER TABLE speakers
ADD COLUMN embedding BLOB
""")

conn.commit()
conn.close()

print("✅ embedding column added to speakers table!")
