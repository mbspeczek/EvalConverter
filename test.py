from types import resolve_bases
import unittest
from unittest import result
from app import SimpleGeoFigCalc, UniversalConverter

class TestStringMethods(unittest.TestCase):

    def test_UniversalConverter_convert_celcius_to_farenheit(self):
        # arrange
        dict = {"test":"a*a"}
        a = UniversalConverter(dict)
        # act
        test = a.convert_celcius_to_farenheit(10)
        # assert
        self.assertEqual(test,50)
        self.assertEqual(a.convert_celcius_to_farenheit(-1000),None)

    def test_UniversalConverter_convert_celcius_to_kelvin(self):
        # arange
        dict = {"test":"a*a"}
        a = UniversalConverter(dict)
        # act 
        result = a.convert_celcius_to_kelvin(10)
        result2 = a.convert_celcius_to_kelvin(-4000)
        # assert
        self.assertEqual(result,283.15)
        self.assertEqual(result2,None)
        self.assertTrue(a.convert_celcius_to_kelvin(-273)) # min value is -273.15
        self.assertFalse(a.convert_celcius_to_kelvin(-274))

    def test_UniversalConverter_convert_meters_to_km(self):
        # arange
        a = UniversalConverter({"test":"a*a"})
        # act
        result = a.convert_meters_to_km(1000)
        # assert
        self.assertEqual(result, 1)
        self.assertEqual(a.convert_meters_to_km(-3),-1)
        self.assertEqual(a.convert_meters_to_km(0),0)


    def test_UniversalConverter_convert_squareMeters_to_squareFeet(self):
        # arange
        a = UniversalConverter({"test":"a*a"})
        # act
        result = a.convert_squareMeters_to_squareFeet(10)
        # assert
        self.assertEqual(result, a.convert_squareMeters_to_squareFeet(10))
        self.assertEqual(a.convert_squareMeters_to_squareFeet(-1),-1)
        self.assertEqual(a.convert_squareMeters_to_squareFeet(0),0)

    def test_UniversalConverter_convert_bits_to_bytes(self):
        # arange
        a = UniversalConverter({"test":"a*a"})
        # act
        result = a.convert_bits_to_bytes(13)
        # assert
        self.assertEqual(result, "1 byte and 5 bits")
        self.assertEqual(a.convert_bits_to_bytes(0),"No bytes")
        self.assertEqual(a.convert_bits_to_bytes("dasd"), "No bytes")

    def test_UniversalConverter_return_converters(self):
        # arange
        a = UniversalConverter({"test":"a*a"})
        # act
        result = a.return_converters()
        # assert
        self.assertEqual(result, ["test"])

    def test_UniversalConverter_multi_convert(self):
        # arange
        a = UniversalConverter({"celcius->farenheit": "(x*1.8)+32"})
        # act
        result = a.multi_convert(10,"celcius->farenheit")
        # assert
        self.assertEqual(result, a.convert_celcius_to_farenheit(10))

    def test_SimpleGeoFigCalc_return_formulas(self):
        # arange
        a = SimpleGeoFigCalc({"square":"v1*v1"})
        # act
        result = a.return_formulas()
        # assert
        self.assertEqual(result, ["square"])

    def test_SimpleGeoFigCalc_add_new_formula(self):
        # arange
        a = SimpleGeoFigCalc({"square":"v1*v1"})
        # act
        a.add_new_formula(("test","v1*v2")) # dict is sorted by keys
        result = a.return_formulas()
        # assert
        self.assertEqual(result, ["square","test"])

    def test_SimpleGeoFigCalc_solve_triagnleArea(self):
        # arange
        a = SimpleGeoFigCalc({"triangle-area":"v1*v2/2"})
        # act
        result = a.solve("triangle-area",["v1","v2"],[3,2])
        # assert
        self.assertEqual(result, 3)
    
    def test_SimpleGeoFigCalc_solve_rectangleArea(self):
        # arange
        a = SimpleGeoFigCalc({"rectangle-area":"v1*v2"})
        # act
        result = a.solve("rectangle-area",["v1","v2"],[3,2])
        # assert
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
