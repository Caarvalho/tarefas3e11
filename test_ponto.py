import unittest
import ponto

class testPonto(unittest.TestCase):
       
    def test_getX(self):
        p = ponto.Ponto(1,2)
        self.assertEqual(p.getX(), 1)

    def test_getY(self):
        p = ponto.Ponto(1,2)
        self.assertEqual(p.getY(), 2)
    
    def test_setX(self):
        p = ponto.Ponto(1,2)
        p.setX(2)
        self.assertEqual(p.getX(), 2)
    
    def test_setY(self):
        p = ponto.Ponto(1,2)
        p.setY(3)
        self.assertEqual(p.getY(), 3)
    
    def test_qualQuadrante(self):
        p = ponto.Ponto(1,2)
        self.assertEqual(p.qualQuadrante(), 1)



if __name__=="__main__":
    unittest.main()