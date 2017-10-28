import re
from datetime import datetime
if __name__=="__main__":

    # Домашнее задание Урок 3 . задание 1

    # s = input("Enter words without speces: ")
    # s= "abcdefjh"
    # print (s)
    # print("1row=",s[2])
    # print("2row=",s[-1])
    # print("3row=",s[0:4])
    # print("4row=",s[0:-2])
    # print("5row=",s[0::2])
    # print("6row=",s[1::2])
    # print("7row=",s[::-1])
    # print("8row=",s[::-2])


    # Домашнее задание Урок 3 . задание 2
    # s= "abcdefjh4"
    # print(s)
    # print(len(s))
    #
    # if ((len(s)%2)>0):
    #
    #     i =int((len(s)-1)/2+1)
    #     print("p1=",i)
    # else:
    #     i = int (len(s)/2)
    #     print("p2=", i)
    #
    # print (s[0:i]  , " + " ,  s[i+1:])


    # Домашнее задание Урок 3 .  Задание 3   1)	Напишите счетчик с помощью конструкции while, который выводит числа от 0 до 10.
    # x=0
    # while x<=10:
    #    print (x)
    #    x+=1

    # Домашнее задание Урок 3 . Задание 3   2)	Напишите счетчик с помощью конструкции while, который выводит числа от 20 до 1.
    # x=20
    # while x>=0:
    #    print (x)
    #    x-=1

    # Задание 4
    # У вас есть список чисел.
    # 1.	Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым
    # 3.	Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького до самого большого, пока он не останется пустым.

    # Домашнее задание Урок 3 . Задание 4. 1.	Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым
    # l=[8,5,7,2,1,4,6,10,20,17]
    # print (l)
    # i=0
    # while i<len(l) :
    #     l.remove(l[i])
    #     print (l)


    # Домашнее задание Урок 3 . Задание 4. 2.	** Как сделать это же задание со строкой?
    # s= "Привет медвед! "
    # print(len(s))
    # i=0
    # n=len(s)
    # while i+1<n:
    #     s= s[1:len(s)]
    #     i+=1
    #     print(s)
    # print("Итоговая строка = " ,s , " ?")

    # Домашнее задание Урок 3 . Задание 4. 3. Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького до самого большого, пока он не останется пустым.

    # l=[8,5,7,2,1,4,6,10,20,17]
    # print (l)
    # while len(l)>0:
    #     print(l.pop(0))
    # print ("Final list is: ",l)

    # Задание 4
    # Создайте строку, в которой написан, какой-то текст. Пример:
    # We are not what we should be! We are not what we need to be. But at least we are not what we used to bе  (Football Coach)
    # •	Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
    # •	Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
    # •	Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
    # Усложнённое ** (можно сначала его не делать):
    # •	Посчитать, сколько раз встречается каждое слово.
    # (Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях подсчитываем количество «встречаний» этого слова)


    # s="We are not what we should be! We are not what we need to be.But at least we are not what we used to bе (Football Coach)"
    # l= (s.split())
    # print ("В выражении ",len(l)," слов")
    # l= re.findall('[a-zA-Z]+', s)# import calendar
    # def is_year_leap (year ):
    #     if (year is None ): year=datetime.now().year
    #     year = int(year)
    #     if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    #        return 1
    #     else:
    #         return 0
    # def is_year_leap2 ( year ) :
    #     if (year is None): year = datetime.now().year
    #     d= str(year)+"-02"
    #     date  = datetime.strptime(d,'%Y-%m')
    #     dates = calendar.monthrange( date.year, date.month)[1]
    #     if dates==29:
    #         return 1
    #     else:
    #         return 0
    # print(is_year_leap2 (2016))
    # print(is_year_leap2 (2017))
    #
    # print(is_year_leap (2016))
    # print(is_year_leap (2017))

    # print("Строка без знаков спец символов и знаков: ",*l)
    # l.sort( reverse=False)
    # print("Отсортированная строка: ",*l)

    # print (datetime.strptime( "2009", "%Y" ))
    # print(datetime.strptime( "2009-02", "%Y-%m" ).isocalendar())


    # Задание 6
    # Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).
    #
    # def triangle (a,b,c):
    #     if (a is  None or b is  None or c is  None ):
    #         return -1
    #     else :
    #         try:
    #             a=float(a)
    #             b=float(b)
    #             c=float(c)
    #             if ( (a+b)>c and (a+c)>b and (b+c)>a ):
    #                 if a==b==c :
    #                     return "Equilateral triangle"
    #                 elif a==b or b==c or a==c :
    #                     return "Isosceles triangle"
    #                 elif a!=b and b!=c and a!=c :
    #                     return "Versatile triangle"
    #             else: return "Not a triangle"
    #         except Exception as e:
    #             return e
    #
    # print (triangle (1.1,1.1,1.1))
    # print (triangle (2.5,2.5,1))
    # print (triangle (4.5,5.1,2.3))
    # print (triangle (0,0,0))
    # print (triangle ("1",0,0))
    # print (triangle ([1,2],0,0))
    #

    # Задание 7
    # Пишем функцию, которая выводим второе по возрастанию значение из переданных аргументов. Учитываем, что может быть повторяющиеся значения аргументов.
    #
    # def f_sort (*args):
    #     l= [*args]
    #     l.sort()
    #     # print (l) # отладочная строка
    #     i=0
    #     while  i<len(l):
    #         if l[i] == l[i+1]:
    #             return " Element=" + str(l[i]) + " position=" + str(i)
    #         i=i+1
    #     return 0
    #
    # print ( f_sort(1,5,2,2,3,7) )
    # print ( f_sort(1,5,2,2,1,7) )
    # print ( f_sort(8,-4,2,1,5,8,5) )
    # print ( f_sort(8,-4,2,1,5,8) )


    # Задание 8
    # Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
    # 1-е число – сколько строк будет в песне. По умолчанию 3
    # 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
    # 3-е число – если 0, то в конце стоит точка, если 1, то в конце стоит «!». По умолчанию 0

    def f_lala (row_count =3 ,word_count =3, last_s=0 ):
        i=1
        j=1
        s=""
        while  j<=row_count :
            while i<=word_count:
                if i<word_count:
                    s=s+"la-"
                else:
                    s=s+"la"
                i=i+1
                #print(s)
            i=1
            if j== row_count:
                if last_s==0 :
                    s= s+"."
                else:
                    s= s+"!"
            else:
                s = s + '\n'
            j = j + 1
        return s

    print (f_lala(5,4,1))
    print (f_lala(3,6,0))