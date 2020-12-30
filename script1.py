import sqlite3
import json

conn = sqlite3.connect("users.info")
cur= conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store ('users.json')")
conn.commit()
conn.close()



cur.execute("CREATE TABLE IF NOT EXISTS store ('users.json')")
conn.commit()
conn.close()
