import yaml

# YAML 정의하기
yaml_str = """
Date : 2021-03-18
PriceList :
    -
        item_id : 100
        name : Apple
        color : red
        price : 800
    -
        item_id : 101
        name : Banana
        color : yellow
        price : 550
    -
        item_id : 102
        name : Strawberry
        color : red
        price : 900 
"""

# YAML 분석하기
data = yaml.load(yaml_str)

# 이름과 가격 출력하기
for item in data["PriceList"]:
    print(item["name"], item["price"])