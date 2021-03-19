import sqlite3

# DB 연결하기
dbpath = "test2.sqlite"
conn = sqlite3.connect(dbpath)

# 테이블 생성하기
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER)""")
conn.commit()

# 데이터 넣기
cur = conn.cursor()
cur.execute(
    "INSERT INTO items (name, price) VALUES (?, ?)",
    ("Orange", 5200))
conn.commit()

# 데이터 연속으로 넣기
cur = conn.cursor()
data = [("Mango", 7700), ("Kiwi", 4000), ("Grape", 8000),
    ("Peach", 9400), ("Persimon", 7000), ("Strawberry", 4000)]
cur.executemany(
    "INSERT INTO items (name, price) VALUES (?, ?)",
    data
)
conn.commit()

# 4000~7000 사이의 데이터만 추출하기
cur = conn.cursor()
price_range = (4000, 7000)
cur.execute(
    "SELECT * FROM items WHERE price>=? AND price<=?",
    price_range)
item_list = cur.fetchall()
for item in item_list:
    print(item)