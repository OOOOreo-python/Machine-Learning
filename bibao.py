def FunX(x):
    def FunY(y):
        return x*y
    return FunY    #内部函数FunY就是一个闭包

