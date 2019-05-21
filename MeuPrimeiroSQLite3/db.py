import sqlite3

conn = sqlite3.connect('shallownowschool.db')

cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM TB_ESTUDANTE;
""")

for linha in cursor.fetchall():
    print(linha)


conn.close()
