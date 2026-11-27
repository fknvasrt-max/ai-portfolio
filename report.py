import pandas as pd

df = pd.read_excel("sales.xlsx")

summary = df.groupby(["销售员", "日期"], as_index=False)["成交额"].sum()
summary.to_excel("sales_summary.xlsx", index=False)
print("按销售员和日期汇总：")
print(summary)

fuzhou = df[df["地区"] == "福州"]
fuzhou_summary = fuzhou.groupby(["销售员", "日期"], as_index=False)["成交额"].sum()
print("只看福州：")
print(fuzhou_summary)

region = df.groupby("地区", as_index=False)["成交额"].sum()
print("按地区汇总：")
print(region)