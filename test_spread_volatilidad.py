



import unittest

from spread_volatilidad import SpreadVolatilidad


class TestParidadPutCall(unittest.TestCase):
    def setUp(self):
        # Initialize SinteticoMaker instance
        self.SV = SpreadVolatilidad()

    def test_long_stradle(self):
        # compras un call y un put, mismo ejercicio, misma fecha de vencimiento, mismo subyacente, misma cantidad.
        # X1=1150, c=$296, p= $114
        # la maxima perdida se da cuando la opción se cancela en el strike de compra

        first_prima = 296; second_prima = 114; strike = 1150

        expected_result = {"maxima_ganancia" : "ilimitada", "maxima_perdida": 410, "break_even_point_inferior": 740, "break_even_point_superior": 1560}

        result = self.SV.long_stradle(first_prima, second_prima, strike)

        self.assertEqual(result, expected_result)

    def test_short_stradle(self):
        first_prima = 4.15; second_prima = 2.75; strike = 35; 

        expected_result = {"maxima_ganancia" : 6.9, "maxima_perdida": "ilimitada", "break_even_point_inferior": 41.90, "break_even_point_superior": 28.1}

        result = self.SV.short_stradle(first_prima, second_prima, strike)

        self.assertEqual(result, expected_result)

    def test_long_strangle(self):
        #  put GGAL X1=1033; p=75,88; call gal X2=$1250, c=$260
        # Ganancia a partir de valores menores al BEP menor y mayores al BEP mayor

        call_long = {"strike": 1250, "prima": 260}
        put_long = {"strike": 1033, "prima": 75.88}

        expected_result = {"maxima_ganancia" : "ilimitada", "maxima_perdida": 335.88, "break_even_point_inferior": 697.12, "break_even_point_superior": 1585.88}

        result = self.SV.long_strangle(call_long, put_long)

        self.assertEqual(result, expected_result)

    def test_short_strangle(self):
        # vendes un call y un put, mismo ejercicio, misma fecha de vencimiento, mismo subyacente, misma cantidad.
        # X1=1150, c=$296, p= $114
        first_prima = 296; second_prima = 114; strike = 1150
        expected_result = {"maxima_ganancia" : 410, "maxima_perdida": "ilimitada", "break_even_point_inferior": 1560, "break_even_point_superior": 740}

        result = self.SV.short_strangle(first_prima, second_prima, strike)

        self.assertEqual(result, expected_result)
        











if __name__ == '__main__':
    unittest.main()
