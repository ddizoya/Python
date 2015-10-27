__author__ = 'ddizoya'


class Cadena:
    def __init__(self, str):
        self.str = str

    def incrustrar(self):
        tam = len(self.str)
        corch=""
        for i in range(tam):
            if i == 0:
                corch = corch + "{}"
            elif i==tam:
                corch = corch +",'"
            else:
                corch = corch + ",{}"
        str2 = corch.format(*self.str)
        print(str2)

        #Otra forma de hacerlo si el tama?o no es variable
        #print('{},{},{},{}'.format(*self.str))








def main():
    obj = Cadena("Cadena1");
    obj.incrustrar()

if __name__ == '__main__':
    main()