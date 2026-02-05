# 列表推导式：生成 1 到 10 的平方数
squares = [x**2 for x in range(1, 11)]

# Map + Lambda：统一前缀
names = ["张三", "李四", "王五"]
prefixed_names = list(map(lambda name: "QG_" + name, names))

# 实现自动跳过非数字项、仅保留≥80 数值、归一化为 0.xx-1.xx 小数，且根据结果是否 > 1.0
# 对应报「核心过载」或输出「运转正常」
raw_data = ["\ufeff90", "\u0000", "\u001F", " ", "\t\n\r"]

def clean(x):
    """
    使用 float(x) 以兼容 '1e2' 等格式，
    然后再转 int筛选 >= 80 的数值。
    """
    try:
        val = int(float(x)) 
        return val if val >= 80 else None
    except (ValueError, OverflowError):
        return None

clean_list = [clean(x) for x in raw_data if clean(x) != None]

# 直接在推导式中完成：计算 -> 状态判断 -> 格式化
final_results = [
    f"{val / 100:.2f} - {'核心过载' if val / 100 > 1.0 else '运转正常'}"
    for val in clean_list
]

# 最终结果输出
if len(final_results) == 0:
    print("无正常数据")
else:
    print(final_results)