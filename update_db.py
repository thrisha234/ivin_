import sqlite3

conn = sqlite3.connect("db/meetings.db")
c = conn.cursor()

c.execute("ALTER TABLE action_items ADD COLUMN responsible TEXT;")
c.execute("ALTER TABLE action_items ADD COLUMN due_date TEXT;")
c.execute("ALTER TABLE action_items ADD COLUMN challenges TEXT;")

conn.commit()
conn.close()

print("✅ Columns Added Successfully")
