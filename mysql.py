import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root',db='match')
cur = conn.cursor()
cur.execute("SELECT * FROM craw_match")

for r in cur.fetchall():
           print(r)

cur.close()

conn.close()