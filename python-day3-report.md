# Python 第 3 课

写了销售日报汇总脚本 `report.py`，并用 `python3` 运行成功。

- pandas：Python 里专门处理表格的工具，可以读写 Excel
- `read_excel`：打开 Excel，读成一张表
- 筛选：`df[df["地区"] == "福州"]` 只留下符合条件的行
- `groupby`：按销售员、日期或地区分组，再用 `sum()` 把成交额加总
- `to_excel`：把汇总结果导出成新的 Excel
- 先用 `make_sales.py` 生成了模拟的销售日报 `sales.xlsx`
