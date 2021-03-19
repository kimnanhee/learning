# tinydb 버전 3.15.1
from tinydb import TinyDB, Query

# DB 연결하기
dbpath = "test-tinydb.json"
db = TinyDB(dbpath)

# 기존의 테이블 제거하기
db.purge_table('fruits')

# 테이블 생성, 추출하기
table = db.table('fruits')

# 테이블에 데이터 추가하기
table.insert( {"name" : "Cheese Ball", "price" : 5000} )
table.insert( {"name" : "Chicken", "price" : 17000} )
table.insert( {"name" : "Pizza", "price" : 32000} )
table.insert( {"name" : "Cola", "price" : 1500} )
table.insert( {"name" : "Ramyeon", "price" : 3000} )

# 모든 데이터를 추출해서 출력하기
print(table.all())

# 특정 데이터 추출하기
# Chicken 검색하기
Item = Query()
res = table.search(Item.name == "Chicken")
print('Chicken is ', res[0]['price'])

# 가격이 8000원 이상인 것 추출하기
print("8000원 이상의 가격")
res = table.search(Item.price >= 8000)
for i in res:
    print("-", i['name'])