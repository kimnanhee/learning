import yaml

# 파이썬 데이터를 YAML 데이터로 출력하기
customer = [
    {"name" : "nanhee", "age" : "18", "gender" : "woman"},
    {"name" : "minyoung", "age" : "20", "gender" : "woman"},
    {"name" : "choyeon", "age" : "19", "gender" : "woman"},
    {"name" : "hayeon", "age" : "19", "gender" : "woman"}
]
print(customer)

# 파이썬 데이터를 YAML 데이터로 변환하기
yaml_str = yaml.dump(customer)
print(yaml_str)

# YAML 데이터를 파이썬 데이터로 변환하기
data = yaml.load(yaml_str)

for i in data:
    print(i["name"])