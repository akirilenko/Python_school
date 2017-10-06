# x=[1,10,3,5,6,7,11]
# while len(x)!=0 :
#    print (x.pop())
#    print(x)
# вариант реализации №2

# x=[1,10,3,5,6,7,11]
# while x :
#     print (x.pop())
#     print(x)

# l=[1,10,3,5,6,7,11]
# for item in l:
#     if (item%2==0) :
#         print(item)
#     else : print (item+1)

# l=[3,4,3,5,6,7,11]
# print(l)
# for item in l:
#     if (item%2==0) :
#         print(item , "index = ", l.index(item))
#     else :
#         print (item+1,"index = ", l.index(item))
#         l[l.index(item)] =item+1
# print(l)

# for i in range(10):
#     print("i = ",i)


# l=[3,4,3,5,6,7,11]
# print(l)
# for i in range(len(l)):
#     print("i = ", i , " item = ", l[i])
#     l[i] =300
# print(l)


# l=[9,4,1,7,12,5,10]
# print(l)
# for i in range(len(l)):
#     if (l[i]%2==0) :
#         print("i = ", i, " item = ", l[i])
#     else :
#         l[i] = l[i] + 1
#         print("i = ", i, " item = ", l[i])
# print(l)

# print(range(10))
# print(list(range(10)))
# print(list(range(2,10,3)))

# def repeat(s,exclaim):
#     result=s*3
#     if exclaim:
#         result = result +"!!!!!"
#     return result
#
# print(__name__)
#
# if __name__=="__main__":
#      print (repeat ("wow",True))
#      print(__name__)
#

# r = repeat ("wow",True)
# print(r)

# этот пример даст сообщение об ошибке
# r = repeat (5,True)
# print(r)
# import math
# def triangle(a,b) :
#     c = math.sqrt(a * a + b * b)
#     return c
# print("Гипотенуза = ", triangle(2,2) )

# варианты создания функций с не определенным количеством входящих параметров. Тут мы не можем сделать ввод параметров по имени
# def func(*args) :
#     print (args)
#
#
# print(func(1))
# print(func(1,2,3,3))
# print(func())

#вариант
# def func(a,b,*ll) :
#     ll=ll+a+b
#
# print (args)

# def func(**kwargs):
#     return  kwargs.get('name') +' is ' + kwargs.get('job')
#
# print(func(name="Bob",job="HZ"))

s = input('Enter value: ')
try:
    s = int(s)
except:
    print('Error')

