## pandas库的导入

```python
import pandas as pd
```
---
##  读取数据

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
## 简单的数据清洗

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
| **命令**                                 | **作用**              | **C 语言类比**      |
| -------------------------------------- | ------------------- | --------------- |
| `df.info()`                            | 查看每一列的数据类型、是否有空值    | 检查结构体定义和内存分配    |
| `df.describe()`                        | 查看数值列的统计信息（均值、最大值等） | 快速遍历数组找 Max/Min |
| `df["ocean_proximity"].value_counts()` | 查看某个分类列的分布情况        | 统计枚举值的频率        |
|                                        |                     |                 |
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
## 数据保存

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
