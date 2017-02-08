#coding:utf-8

if __name__ == '__main__':
    import sqlite3
    import os
    import codecs
    import json
    import sys

    jsonname = sys.argv[1]
    dbname = sys.argv[2]

    os.chdir("ResultDir")
    with codecs.open(jsonname, "r", "utf-8") as f:
        jsonFILE = json.load(f)
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    data = []
    for j in jsonFILE:
        data.append((j["screenName"], j["tweetID"]))
    insert_sql = "insert into data (screenName, tweetID) values (?, ?)"
    c.executemany(insert_sql, data)
    conn.commit()

    select_sql = "select * from data"
    for row in c.execute(select_sql):
        print row

    conn.close()
