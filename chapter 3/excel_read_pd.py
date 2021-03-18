import pandas as pd

# 엑셀 파일 열기
filename = "people.xlsx"
sheet_name = "person"
book = pd.read_excel(filename, sheet_name=sheet_name, header=1)
print(book)

# 정렬하기
# book = book.sort_values(by=2018, ascending=False)
# print(book)