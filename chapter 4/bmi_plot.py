import matplotlib.pyplot as plt
import pandas as pd

# 키와 몸무게 데이터 읽어 들이기
tbl = pd.read_csv("bmi.csv", index_col=2)

# 그래프 그리기 시작
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# 서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b["weight"],b["height"], c=color, label=lbl)

scatter("fat", "red")
scatter("normal", "green")
scatter("thin", "blue")

ax.legend()
plt.savefig("bmi_plot.png")
plt.show()