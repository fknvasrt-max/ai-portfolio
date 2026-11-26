customers = [
    {"name": "小林", "level": "高意向", "city": "福州"},
    {"name": "小陈", "level": "中意向", "city": "厦门"},
    {"name": "小王", "level": "高意向", "city": "福州"},
    {"name": "小李", "level": "低意向", "city": "厦门"},
    {"name": "小张", "level": "中意向", "city": "福州"},
]

def classify_by_level(customers):
    high = []
    mid = []
    low = []
    for c in customers:
        if c["level"] == "高意向":
            high.append(c["name"])
        elif c["level"] == "中意向":
            mid.append(c["name"])
        else:
            low.append(c["name"])
    return high, mid, low

high, mid, low = classify_by_level(customers)
print("高意向：", high)
print("中意向：", mid)
print("低意向：", low)

fuzhou = []
xiamen = []
for c in customers:
    if c["city"] == "福州":
        fuzhou.append(c["name"])
    else:
        xiamen.append(c["name"])

print("福州：", fuzhou)
print("厦门：", xiamen)