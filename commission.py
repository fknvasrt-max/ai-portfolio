sales = float(input("请输入销售额："))
rate = float(input("请输入提成比例（例如 0.1 表示 10%）："))
commission = sales * rate
print("本笔提成是：", commission)