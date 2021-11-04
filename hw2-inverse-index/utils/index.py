import json
from . import splitter
import sqlite3

def reverse_index(wiki_path='src/wiki_2021_10_05_50000.json', db='mydb.db'):
    # create database
    # _create_db(db)

    # insert wiki information to database
    conn = sqlite3.connect(db)
    c = conn.cursor()
    mysplitter = splitter.Splitter()
    data = json.load(open(wiki_path, 'r', encoding='utf-8'))
    count = 36620
    for doc in data[count:]:
        count += 1
        if count % 10 == 0:
            print(f'Doing the {count} doc.')
        words = mysplitter.split([doc['articles']])
        word_id_pairs = [(w, doc['id']) for w in words[0]]
        c.executemany("INSERT INTO reverse_index VALUES (?, ?)", word_id_pairs)
        conn.commit()
    c.close()
    conn.close()

def _create_db(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''CREATE TABLE reverse_index
                 (word TEXT NOT NULL,
                 doc_id INTEGER NOT NULL)''')
    conn.commit()
    c.close()
    conn.close()