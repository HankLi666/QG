# 截获一条杂乱情报： " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;Mission:2025-RESCUE-X "
# 请运用所有所学知识清洗数据：利用 String 方法去除干扰空格；利用 Set 帮特工去除重复装备；
# 利用 Slicing 截取核心任务代号；利用 Tuple锁定坐标；最后将所有信息归档进一个 Dict档案中

data=" Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X "
#利用strip去除干扰空格
clean_data=data.strip()
#split分割
separate_data=clean_data.split("; ")
#集合去重
items=set(separate_data[2].split(":")[1].split(",") ) 
#将坐标转换成整型
coords_x=int(separate_data[1].split(":")[1].strip("()").split(",")[0])
coords_y=int(separate_data[1].split(":")[1].strip("()").split(",")[1])
#元组锁定坐标
coords=(coords_x,coords_y)
#slicing截取
mission_val = separate_data[3].split(":")[1][5:]
#字典归档
achieve={
    "Agent":separate_data[0].split(":")[1],
    "Coords":coords,
    "Items":items,
    "Mission":mission_val
}
print(achieve)