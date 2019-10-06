# g = lambda x:2*x+1
#
# print(g(5))
#
# f = lambda x,y:x+y
# print(f(1,2))
#
#
# def jiecheng(n):
#     result = n
#     for i in range(1,n):
#         result *= 1
#
#     return result
# number = int(input('输入一个正整数： '))
#
# result = jiecheng(number)

def digui(n):
    if n == 1:
        return 1
    else:
        return n*digui(n-1)

number = int(input('输入一个正整数： '))
result = digui(number)

print('阶乘的结果是',result)
