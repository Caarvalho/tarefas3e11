class Ponto:
    def __init__(self, x, y):
        self._x = x
        self._y = y

   
    def getX(self):
        return self._x

    
    def getY(self):
        return self._y
    
   
    def setX(self, x):
        self._x = x

    
    def setY(self, y):
        self._y = y


    def qualQuadrante(self):
        if self.getX() != 0 and self.getY() != 0:
            if self.getX() > 0 and self.getY() > 0:
                print('Ponto corresponde ao primeiro quadrante.')
                return 1
            elif self.getX() < 0 and self.getY() > 0:
                print('Ponto corresponde ao segundo quadrante.')
                return 2
            elif self.getX() < 0 and self.getY() < 0:
                print('Ponto corresponde ao terceiro quadrante.')
                return 3
            elif self.getX() > 0 and self.getY() < 0:
                print('Ponto corresponde ao quarto quadrante.')
                return 4
        else:
            print('O ponto corresponde ao centro, ou seja, nenhum quadrante.')
            return 0






