import json

price = {
    "date" : "2021-03-18",
    "price" : {
        "Apple" : 80,
        "banana" : 55,
        "Strawberry" : 90
    }
}

s = json.dumps(price)
print(s)