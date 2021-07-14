import sqlite3


path = './db.sqlite3'
conn = sqlite3.connect(path)
cur = conn.cursor()

cur.execute("SELECT * FROM hint_theme")
read2 = cur.fetchall()
for i in read2:
    if i[-1] == 40:
        cur.execute("UPDATE hint_theme SET roomEscape_id = ? WHERE id = ?", (38, i[0]))
    conn.commit()
