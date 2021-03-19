import sqlite3

# sqlite DB 연결하기
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

# 테이블을 생성하고 데이터 넣기
cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;

CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

INSERT INTO items (name, price) VALUES ('Apple', 800);
INSERT INTO items (name, price) VALUES ('Banana', 500);
INSERT INTO items (name, price) VALUES ('Peach', 1000);
""")

# DB 업데이트
conn.commit()

# 데이터 추출하기
cur = conn.cursor()
cur.execute("SELECT item_id, name, price FROM items")
item_list = cur.fetchall()

# 출력하기
for item in item_list:
    print(item)