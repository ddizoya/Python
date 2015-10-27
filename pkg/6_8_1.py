__author__ = 'ddizoya'

class Cadena:
    def __init__(self, str):
        self.str = str

    def impDosPrimCar(self):
        print(self.str[0:2])

    def tresUltimos(self):
        print(self.str[-3:])

    def cadaDosCar(self):
        print(self.str[::2])

    def delReves(self):
        print(self.str[::-1])

    def normalConInverso(self):
        print(self.str[:]+self.str[::-1])




















def main():
    obj = Cadena ("Hola")
    obj.impDosPrimCar()
    obj.tresUltimos()
    obj.cadaDosCar()
    obj.delReves()
    obj.normalConInverso()


if __name__ == '__main__':
    main()