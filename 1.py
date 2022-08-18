#1
import calendar
from math import pi
class Soda:
    def aa (self,a=None):
        if a is not None:
            print(f"У вас газировка с {a} вкусом")
        else:
            print(f"Просто газировка")
soda_1=Soda()
soda_1.aa()
#2
class Math:
    def __init__(self,a:int,b:int):
        self.a=a
        self.b=b
    def addition(self):
        print( f"{self.a+self.b}")
    def multiplication(self):
        print(f"{self.a*self.b}")
    def division(self):
        print(f"{self.a/self.b}")
    def subtraction(self):
        print(f"{self.a-self.b}")
Math_1=Math(2,3)
Math_1.addition()
Math_1.multiplication()
Math_1.division()
Math_1.subtraction()
#3
class Car:
    def __init__(self,color:str,type:str,year:int):
        self.color=color
        self.type=type
        self.year=year
    def Start_engin(self):
        print(f"Автомобиль заведен")
    def Stop_engin(self):
        print(f"Автомобиль заглушен")
    def Year_auto(self):
        print(f"Год выпуска авто: {self.year}")
    def Type_auto(self):
        print(f"Тип авто: {self.type}")
    def Color_auto(self):
        print(f"Цвет авто: {self.color}")
Car_1=Car("green","sedan",2021)
Car_1.Start_engin()
Car_1.Stop_engin()
Car_1.Year_auto()
Car_1.Color_auto()
Car_1.Type_auto()
#4
class Sphere:
    def __init__(self, *arg):
        if len(arg) == 0:
            arg = (1, 0, 0, 0)
        elif len(arg) == 1:
            arg = (arg[0], 0, 0, 0)
        else:
            self.r, self.x, self.y, self.z = arg

    def get_volume(self):
        return (self.r ** 3) * pi * 4 / 3

    def get_square(self):
        return (self.r ** 2) * pi * 4

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 < self.r ** 2
#5
class SuperStr(str):
    def is_repeatance(self, s):
        if not isinstance(s, str):
            return  False
        n = len(self) // (len(s) or 1)
        return self == n * s
    def is_palindrome(self):
        s = self.lower()
        return s == s[::-1]
sup = SuperStr('123123123123')
sup.is_repeatance('123')
sup.is_repeatance('123123')
sup.is_repeatance('123123123123')
sup.is_repeatance('12312')
sup.is_repeatance(123)
sup.is_palindrome()
sup = SuperStr('123_321')
sup.is_palindrome()
#6
def create_calendar_page(m=8, y=2022):
    import calendar
    s=''
    lin='--- - ----------------\nMO TU WE TH FR SA SU\n--------------------\n'
    c = calendar.Calendar()
    for i in c.monthdayscalendar(y, m):
        for q in i:
            q=str(q)
            if q=='0' : q=q.replace('0', '  ')
            if len(q)==1: q =' 0'+q
            s=s+q+' '
        s=s+'\n '
    s=s.replace(' \n', '\n')
    return lin+s
print(create_calendar_page())

import calendar

c = calendar.TextCalendar()
print(c.formatmonth(2019, 1))