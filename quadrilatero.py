from ponto import Ponto

class Quadrilatero():
    @classmethod
    def __init__(cls, p1, p2):
        cls.p1 = p1
        cls.p2 = p2
    
    @classmethod
    def getP1(cls):
        return cls.p1
    
    @classmethod
    def getP2(cls):
        return cls.p2
    
    @classmethod
    def setP1(cls, p):
        cls.p1 = p
    
    @classmethod
    def setP2(cls, p):
        cls.p2 = p

    
    def contidoEmQ(cls, p):
        if  cls.getP1().getX() < cls.getP2().getX() and cls.getP1().getY() > cls.getP2().getY():
            if (p.getX() >= cls.getP1().getX() and p.getX() <= cls.getP2().getX()) and  (p.getY() <= cls.getP1().getY() and p.getY() >= cls.getP2().getY()):
                print('Ponto está contido.')
                return True
            else:
                print('Não está contido.')
                return False
        else:
            print('Não forma a figura desejada, um retangulo.')
            return 0


