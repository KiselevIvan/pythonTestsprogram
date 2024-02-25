'''
Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
'''

class TriangleChecker():
    def __init__(self,*lines):
        self.lines=lines

    def is_triangle(self):
        self.result="Ура, можно построить треугольник!"
        for line in self.lines:
            if not self.valueTypeCheck(line):break 
            if not self.positiveCheck(line):break
            if not self.incorrectCountOrNullLengthCheck(line):break
        
        self.triangleRuleCheck()
        return self.result
    
    def triangleRuleCheck(self):
        if self.result=="Ура, можно построить треугольник!":
            a, b, c = sorted(self.lines)
            if not a + b > c:
                self.result="Жаль, но из этого треугольник не сделать"
                return False
            return True

    def incorrectCountOrNullLengthCheck(self,val):
        if len(self.lines)!=3 or val==0:
            self.result="Жаль, но из этого треугольник не сделать"
            return False
        return True
    
    def valueTypeCheck(self,val):
        if not isinstance(val,(int,float)):
            self.result="Нужно вводить только числа!"
            return False
        return True

    def positiveCheck(self,val):
        if val<0:
            self.result="С отрицательными числами ничего не выйдет!"
            return False
        return True

tr= TriangleChecker(2,"w",6)
print(tr.is_triangle())

tr= TriangleChecker(2,-3,6)
print(tr.is_triangle())

tr= TriangleChecker(2,3)
print(tr.is_triangle())

tr= TriangleChecker(0,3,6)
print(tr.is_triangle())

tr= TriangleChecker(2,3,6)
print(tr.is_triangle())

tr= TriangleChecker(3,4,6)
print(tr.is_triangle())

