# 截获一条杂乱情报： " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;Mission:2025-RESCUE-X "
# 请运用所有所学知识清洗数据：利用 String 方法去除干扰空格；利用 Set 帮特工去除重复装备；
# 利用 Slicing 截取核心任务代号；利用 Tuple锁定坐标；最后将所有信息归档进一个 Dict档案中

# 原始数据
data = " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X "

# 1. 利用 strip 去除干扰空格
clean_data = data.strip()

# 2. split 分割逻辑块
parts = clean_data.split("; ")

# 3. 集合去重
items = set(parts[2].split(":")[1].split(","))

# 4. 元组锁定坐标
raw_coords = parts[1].split(":")[1].strip("()")
coords_x, coords_y = raw_coords.split(",")
coords = (int(coords_x), int(coords_y))

# 5. slicing 截取核心代号（2025- 占 5 位，切片从索引 5 开始）
mission_val = parts[3].split(":")[1][5:]

# 6. 字典归档
achieve = {
    "Agent": parts[0].split(":")[1],
    "Coords": coords,
    "Items": items,
    "Mission": mission_val
}

print(achieve)