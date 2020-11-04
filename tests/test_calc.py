import unittest
from calculadora import Calculadora
from io import StringIO

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_perfect(self):
        self.assertIsNotNone(self.calc)

    def test_soma(self):
        self.calc.adiciona(1.0)
        self.assertEqual(1.0, self.calc.valor())

    def test_sub(self):
        self.calc.subtrai(1.0)
        self.assertEqual(-1.0, self.calc.valor())

    def test_multiplica(self):
        self.calc.adiciona(5.0)
        self.calc.multiplica(2.0)
        self.assertEqual(10.0, self.calc.valor())

    def test_divide(self):
        self.calc.adiciona(10.0)
        self.calc.divide(2.0)
        self.assertEqual(5.0, self.calc.valor())

    def test_lista_vazia(self):
        with StringIO() as out:
            self.calc.lista(saída=out)
            result = out.getvalue()
            self.assertFalse(result)

    def test_lista_nao_vazia(self):
        with StringIO() as out:
            self.calc.adiciona(1.0)
            self.calc.subtrai(2.0)
            self.calc.multiplica(3.0)
            self.calc.divide(3.0)
            self.calc.lista(saída=out)
            result = out.getvalue().splitlines()
            print(result)
            self.assertEqual(4, len(result))
            self.assertTrue("+" in result[0])
            self.assertTrue("=" in result[0])
            self.assertTrue("1.0" in result[0])
            self.assertTrue("-" in result[1])
            self.assertTrue("=" in result[1])
            self.assertTrue("- 2.0" in result[1])
            self.assertTrue("\u00D7" in result[2])
            self.assertTrue("=" in result[2])
            self.assertTrue("-3.0" in result[2])
            self.assertTrue("÷" in result[3])
            self.assertTrue("=" in result[3])
            self.assertTrue("-1.0" in result[3])


