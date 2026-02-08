# 设计面向对象思想实现图书库存管理系统，
# 落地类变量、封装、继承、异常处理等需求

class StockError(Exception):
    """用于处理库存相关的逻辑错误"""
    pass

class Books:
    __class_totalcnt = 0
    __class_stockcnt = 0

    def __init__(self, name, amount):
        self.name = name
        self.__totalcnt = amount
        self.__stockcnt = amount
        # 通过 self.__class__ 动态修改“当前类”的统计量
        self.__class__.__class_totalcnt += amount
        self.__class__.__class_stockcnt += amount

    def borrow_book(self, amount):
        if self.__stockcnt >= amount:
            self.__class__.__class_stockcnt -= amount
            self.__stockcnt -= amount
            print(f"成功借出 {amount} 本《{self.name}》")
        else:
            # 使用异常处理
            raise StockError(f"库存不足！'{self.name}' 仅剩 {self.__stockcnt} 本。")

    def put_stock(self, amount):
        self.__class__.__class_totalcnt += amount
        self.__class__.__class_stockcnt += amount
        self.__totalcnt += amount
        self.__stockcnt += amount
        print(f"成功进货 {amount} 本《{self.name}》")

    def return_book(self, amount):
        # 当前库存 + 归还数 如果超过了 该书的总进货量，说明归还数据有误
        if self.__stockcnt + amount <= self.__totalcnt:
            self.__class__.__class_stockcnt += amount
            self.__stockcnt += amount
            print(f"成功归还 {amount} 本《{self.name}》")
        else:
            # 计算一下最多还能还多少本，作为错误提示的一部分
            max_can_return = self.__totalcnt - self.__stockcnt
            raise StockError(
                f"归还失败！《{self.name}》总库存仅为 {self.__totalcnt},"
                f"当前已在库 {self.__stockcnt}，最多只能归还 {max_can_return} 本。"
            )
        
    def get_class_cnt(self):
        return f"共有{self.__class__.__class_totalcnt}本,在库{self.__class__.__class_stockcnt}本"
    
    def get_cnt(self):
        return f"《{self.name}》共有{self.__totalcnt}本,在库{self.__stockcnt}本"

class Science(Books):
    __class_totalcnt = 0
    __class_stockcnt = 0
    def __init__(self, name, amount, ID):
        super().__init__(name, amount)
        self.ID = ID

class Literature(Books):
    __class_totalcnt = 0
    __class_stockcnt = 0
    def __init__(self, name, amount, ID):
        super().__init__(name, amount)
        self.ID = ID

# --- 测试 ---
try:
    p1 = Science('三体', 10, 102912)
    p2 = Literature('鲁迅全集', 5, 102941)
    p3 = Science('Dune', 5, 102912)
    p1.put_stock(10)  
    p1.borrow_book(4) 
    p1.return_book(2)
    
    print(f"科学类在库总量: {p1.get_class_cnt()}")  
    print(f"文学类在库总量: {p2.get_class_cnt()}") 
    print(p1.get_cnt())

except StockError as e:
    print(f"捕获到异常: {e}")