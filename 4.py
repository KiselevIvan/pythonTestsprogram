'''
Строки в Питоне сравниваются на основании значений символов.
Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим.
А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки), а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить).
Такое положение дел не устроило Анну.
Она считает, что строки нужно сравнивать по количеству входящих в них символов.
Для этого девушка создала класс RealString и реализовала озвученный инструментарий. Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного.
'''

class RealString:
    def __init__(self,val):
        self.val=str(val)

    def __gt__(self, other):
        if isinstance(other, RealString):
            return len(self.val) > len(other.val)
        elif isinstance(other, str):
            return len(self.val) > len(other)
        else:    
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self.val) < len(other.val)
        elif isinstance(other, str):
            return len(self.val) > len(other)
        else:
            return NotImplemented


str1 = RealString("Apple")
str2 = RealString("Яблоко")

if str1 < str2:
    print("Строка 1 меньше строки 2")
else:
    print("Строка 1 не меньше строки 2")

if  str2 >"mango":
    print("Строка 2 больше строки mango ")
else: 
    print("Строка 2 не больше строки mango ")

