import csv, codecs

with codecs.open("write.csv", "w", "euc_kr") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "이름", "가격"])
    writer.writerow(["100", "마우스", 110000])
    writer.writerow(["101", "노트북", 2750000])
    writer.writerow(["102", "단팥빵", 1500])