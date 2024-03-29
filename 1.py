'''
Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). 
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
'''

class Soda():
    def __init__(self,additive=None):
        self.additive=additive

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")

def main():
    pepsi=Soda("сахар")
    pepsi.show_my_drink()

    soda=Soda()
    soda.show_my_drink()

main()
