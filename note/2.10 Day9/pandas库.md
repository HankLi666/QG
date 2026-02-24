## pandas库的导入

```python
import pandas as pd
```
---
## 核心结构：Series 与 DataFrame
- **Series**: 一维数组，逻辑上非常像 **Python 字典**（增强版有序字典）。

	- `.index`: 标签（Keys）。
	- `.values`: 实际数据（Numpy 数组）。
- **DataFrame**: 二维表格，由多个 Series 组成，每一列就是一个 Series。
---
##  1.读取数据

Pandas 支持几乎所有主流的数据格式。最常用的是 CSV 和 Excel。

| **函数**            | **说明**      | **示例**                            |
| ----------------- | ----------- | --------------------------------- |
| `pd.read_csv()`   | 读取逗号分隔符文件   | `df = pd.read_csv('data.csv')`    |
| `pd.read_excel()` | 读取 Excel 文件 | `df = pd.read_excel('data.xlsx')` |
| `df.head(n)`      | 查看前 n 行数据   | `df.head(5)`                      |
- `read_csv()`和`read_excel()`可以**直接解析url读取数据**：
```python
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

df = pd.read_csv(url)

# 再将数据存到吗本地
df.to_csv('housing.csv', index=False)
```
- 如果数据**有中文**，需要加上 `encoding='utf-8'` 或 `encoding='gbk'`

```python
df = pd.read_csv('上海房价数据.csv', encoding='utf-8')

# 如果 utf-8 报错，换成 gbk 
df = pd.read_csv('北京公交线路.csv', encoding='gbk')
```
---
## 2.简单的数据清洗

###  处理缺失值 (NaN)

数据中经常会有空洞（Pandas 称之为 `NaN`）。

- **检查空值：** `df.isnull().sum()` （查看每列有多少个空位）。

- **删除空值：** `df.dropna()` （只要有空位的行，通通删掉）。

- **填充空值：** `df.fillna(0)` （把所有空位填成 0）。

### 处理重复数据

- **查找重复：** `df.duplicated()`。

- **删除重复：** `df.drop_duplicates(inplace=True)`。

### 数据筛选与转换

- **选择列：** `df['列名']`。

- **条件筛选：** `df[df['年龄'] > 20]` （筛选年龄大于 20 的所有行）。

- **修改类型：** `df['年龄'] = df['年龄'].astype(int)`。
### 数据分析

| **命令**                                       | **作用**                 | **C 语言类比**                      |
| -------------------------------------------- | ---------------------- | ------------------------------- |
| `df.info()`                                  | 查看每一列的数据类型、是否有空值       | 检查 `struct` 定义和 `malloc` 后的内存分配 |
| `df.describe()`                              | 查看数值列的统计信息（均值、最大值等）    | 快速遍历数组寻找 `Max/Min/Avg`          |
| `df["col"].value_counts()`                   | 查看某个分类列的分布情况           | 遍历数组统计枚举值（Enum）出现的频率            |

#### df.info()报告解析
以[加州房价数据集](https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv) `df.info()`为例
```bash
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 10 columns):
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   longitude           20640 non-null  float64
 1   latitude            20640 non-null  float64
 2   housing_median_age  20640 non-null  float64
 3   total_rooms         20640 non-null  float64
 4   total_bedrooms      20433 non-null  float64
 5   population          20640 non-null  float64
 6   households          20640 non-null  float64
 7   median_income       20640 non-null  float64
 8   median_house_value  20640 non-null  float64
 9   ocean_proximity     20640 non-null  object
dtypes: float64(9), object(1)
memory usage: 1.6+ MB
```

- **RangeIndex:** 数据的行范围（相当于 C 数组下标 `0` 到 `N-1`）。

- **Memory Usage:** 占用的 RAM 大小。深度学习大数据集时，需注意防止内存溢出

- 通过对比 **Total Entries**（总行数）与 **Non-Null Count**（非空数），可以快速定位缺失值：

	- 总行数：`20640 entries` ，`total_bedrooms` 列：`20433 non-null`
	   
	 - **结果：** 该列存在 $20640 - 20433 = 207$ 个空洞（NaN），需处理。
- **注意**：`info()`不返回一个字符串或表格，它会**直接把结果打印到控制台**，不能直接写进文件里面
---
### 数据离散化：pd.cut()
#### 参数说明
```python
pd.cut(x, bins, labels=None, right=True, include_lowest=False)
```

|**参数**|**含义**|**细节**|
|---|---|---|
|**`x`**|待处理的数据|通常是 Series，如 `data['Age']`。|
|**`bins`**|切分规则|可以是**整数**（等宽切分）或**列表**（指定刻度）。|
|**`labels`**|区间名字|必须与区间数量一致。如果不设置，会显示数学区间符号如 `(0, 10]`。|
|**`right`**|闭合方向|`True` 为左开右闭 `(a, b]`；`False` 为左闭右开 `[a, b)`。|
|**`include_lowest`**|包含最小值|配合 `right=True` 使用，确保最小值不会被漏掉。|
#### 两种切分模式

##### 指定刻度

手动定义区间的“边界线”。适用于有明确逻辑的场景（如：兄弟姐妹数量、年龄段）。

```python
# 刻度线：[0, 1, 3, 5] 会产生 3 个区间：0-1, 1-3, 3-5
bins = [0, 1, 3, 5]
data['FamilyType'] = pd.cut(data['SibSp'], bins=bins, labels=['独行', '小家庭', '大家庭'])
```
##### 等宽切分

```python
# 将票价均匀切成 5 份（每份的钱数跨度一样）
data['FareLevel'] = pd.cut(data['Fare'], bins=5)
```
---
### 数据分组统计：groupby()
#### 函数说明
```python
df.groupby(by='A')['B'].value_counts()
```
按 A 分组后，统计 B 列中各值的出现次数
#### 核心流程

执行 `data.groupby('Sex')['Survived'].mean()` 时，发生了三件事：

1. **拆分**：Pandas 扫描 `Sex` 列，根据不同的值（男/女）将原始数据切成一个个独立的“小组”。此时数据还没变，只是分了堆

2. **应用**：每个小组内部，取出 `Survived` 列，运行指定的函数（如 `mean()`、`count()`、`sum()`）

3. **合并**：将各组计算出的结果重新拼接起来，形成一个新的 Series 或 DataFrame
#### 分组后的常见操作

除了 `mean()`，还可以根据需求进行不同的统计：

| **常用函数**       | **作用**       | **泰坦尼克号场景**                                           |
| -------------- | ------------ | ----------------------------------------------------- |
| **`.size()`**  | 统计每组的行数（含空值） | 统计各舱位总人数                                              |
| **`.count()`** | 统计每组非空值的个数   | 统计各年龄段有记录的人数                                          |
| **`.sum()`**   | 求和           | 统计生还者的总人数（因为生还标记是1）                                   |
| **`.agg()`**   | 同时进行多种运算     | `data.groupby('Pclass')['Fare'].agg(['mean', 'max'])` |
#### 多列分组 

可以根据多个维度同时分组，在分析“复合条件”时非常有用

```python
# 示例：同时按“客舱等级”和“性别”分组，看生还率
result = data.groupby(['Pclass', 'Sex'])['Survived'].mean()
```

- **结果**：得到一个“多级索引”。比如一等舱男性、一等舱女性、二等舱男性... 每一个组合都会有一个结果。、
#### observe参数
- **默认 (True)**：哪组有数据就报哪组。如果“80岁以上”这组没人生还，结果里直接就没这一行。

- **设置 False**：如果用 `pd.cut` 定义了 10 个年龄段，那么 `groupby` 就会严格按照这 10 个段点名。即使某段人数是 0，它也会在结果里写上 `0`，而不是直接跳过
---
## 3.数据保存

常用`to_csv()`函数保存
### 基础模板

```python
df.to_csv('filename.csv', index=False, encoding='utf-8-sig')
```
### idex索引
当使用 `df = pd.read_csv()` 读取数据时，Pandas 会自动给每一行分配一个从 0 开始的编号

- 如果设置 **`index=False`**： 保存的文件只包含数据本身。

	**结果：** `longitude, latitude, ...`

- 如果设置 **`index=True`**： Pandas 会把那列 `0, 1, 2, 3...` 的行号也作为一个单独的列存进 CSV。

	**结果：** `, longitude, latitude, ...`（第一列会多出无意义的序号） 
### 其他常用保存格式

| **格式**     | **函数**           | **使用场景**                            |
| ---------- | ---------------- | ----------------------------------- |
| **Excel**  | `df.to_excel()`  | 需要给非技术人员看报告时。                       |
| **JSON**   | `df.to_json()`   | Web 前端交互或配置存储。                      |
| **Pickle** | `df.to_pickle()` | **Python 特有二进制格式。** 保存速度最快，且能保留数据类型 |
