import openpyxl

# 엑셀 파일 열기
filename = "people.xlsx"
book = openpyxl.load_workbook(filename)

# 맨 앞의 시트 추출하기
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출하기
data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[7].value
    ])

# 필요없는 줄 제거
del data[:4]
del data[-1]

# 인구 순서로 정렬하기
data = sorted(data, key=lambda x:x[1])

for i in data[:5]:
    print(i[0], i[1])