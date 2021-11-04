import sqlite3

def retrieve_wiki(keyword, db='mydb.db'):
    if keyword:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute("SELECT DISTINCT * FROM reverse_index WHERE word = ? ORDER BY doc_id", [keyword])
        result = c.fetchall()
        if result:
            print(result[0][0], result[0][1], sep=': ', end=', ')
            for r in result[1:-1]:
                print(r[1], end=', ')
            print(result[-1][1])