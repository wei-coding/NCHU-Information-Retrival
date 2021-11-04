import sqlite3

def retrieve_wiki(keyword, db='mydb.db'):
    if keyword:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute("SELECT * FROM reverse_index WHERE word = ? ORDER BY doc_id", [keyword])
        result = c.fetchall()
        print(result[0][0], end=':')
        for r in result:
            print(r[1], end=' ')