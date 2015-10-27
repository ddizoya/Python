__author__ = 'ddizoya'

class Corcho(object):
    def __init__(self, bodega):
        self.bodega = bodega

class Botella(Corcho):

    def __init__(self, bodega, corcho):
        Corcho.__init__(self, bodega)
        self.corcho = corcho

class Sacacorchos(object):

    def __init__(self):
        self.referencia = []

    def destapar(self, botella):
        if botella.corcho == "none":
            raise "Ya esta destapado"
        elif botella.corcho != "none":
            if self.referencia.count(botella.bodega) >= 1:
                raise "Esta referencia ya esta en uso"
            else:
                self.referencia.append(botella.bodega)
                botella.corcho = "none"


    def limpiar(self, botella):
        for i  in self.referencia:
            print(i)
            if i == botella.bodega:
                self.referencia.remove(i)






def main():
    obj = Botella("e","si")
    obj2 = Botella("e3","si")
    obj3 = Botella("e2","si")

    sc = Sacacorchos()

    sc.destapar(obj)
    sc.destapar(obj2)
    sc.destapar(obj3)


    sc.limpiar(obj)




if __name__ == '__main__':
    main()

