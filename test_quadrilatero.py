import unittest
import quadrilatero
from ponto import Ponto
class TestQuadrilatero(unittest.TestCase):

    def test_getP1(self):
        p1 = Ponto(1,5)
        p2 = Ponto(5,1)
        q = quadrilatero.Quadrilatero(p1, p2)
        self.assertIs(q.getP1(), p1)
    
    def test_getP2(self):
        p1 = Ponto(1,5)
        p2 = Ponto(5,1)
        q = quadrilatero.Quadrilatero(p1, p2)
        self.assertIs(q.getP2(), p2)

    def test_setP1(self):
        p1 = Ponto(1,5)
        p2 = Ponto(5,1)
        p3 = Ponto(2,5)
        q = quadrilatero.Quadrilatero(p1, p2)
        q.setP1(p3)
        self.assertIs(q.getP1(), p3)

    def test_setP2(self):
        p1 = Ponto(1,5)
        p2 = Ponto(5,1)
        p3 = Ponto(2,5)
        q = quadrilatero.Quadrilatero(p1, p2)
        q.setP2(p3)
        self.assertIs(q.getP2(), p3)
    
    def test_contidoEmQ(self):
        p1 = Ponto(1,5)
        p2 = Ponto(5,1)
        p3 = Ponto(2,5)
        q = quadrilatero.Quadrilatero(p1, p2)
        self.assertIs(q.contidoEmQ(p3), True)
    
    
    
    
if __name__ == "__main__":
    unittest.main()
    