# 定义一个迭代器

class MyIterable:
    def __init__(self, start, end):
        self.current = start
        self.end = end
        
    # 返回对象
    # 有__iter__方法表示当前对象可迭代 / 可遍历
    def __iter__(self):
        return self
    
    def __next__(self):
        # 进行判断，抛出，异常迭代结束
        if self.current >= self.end:
            raise StopIteration
        # 获取当前值
        value = self.current
        self.current += 1
        return value
    
if __name__ == '__main__':
    my_iter = MyIterable(1, 10)    
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__())
    print('*'*30)
    for i in my_iter:
        print(i)