import unittest
from HtmlTestRunner import HTMLTestRunner
class OurTestCase(unittest.TestCase):
    def test_metod(self):
        assert result == 1
        # self.assertEqual(4,7)
    def test_metod2(self):
        self.assertEqual(4,4)
# в круглых скобкаж нужно указать имя метода, который создан  вклассе с тестами. Класс OurTestCase, имя метода test_metod
# test1 = OurTestCase("test_metod")
# result = test1.run();
# print (result)

# secord run type
# создем обьест тест сьюта с классом с тестмаи
suite = unittest.TestLoader().loadTestsFromTestCase(OurTestCase)
# создаем обьект  тестового результата. Сейчас он еще пустой
result =  unittest.TestResult()
# запускаем тест сьют, передаем контейнер для сохранения результата - тут его наполняем
suite.run(result)
# печать полученного результата
print(result)

if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner(output=r"C:\Anna\Python_Lecture\TestResult"))
