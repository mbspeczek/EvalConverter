class UniversalConverter:
    def __init__(self, _parserDict):
        self.zeroAbsolute =(-1)*273.15
        self.parserDict = _parserDict

    def ser_new_parserDict(self, _parserDict):
        self.parserDict = _parserDict

    def convert_celcius_to_farenheit(self, _celcius):
        if _celcius > self.zeroAbsolute:
            return ((_celcius*1.8)+32)
        else:
            return "fail"

    def convert_celcius_to_kelvin(self, _celcius):
        if _celcius > self.zeroAbsolute:
            return _celcius + 273.15
        else:
            return "fail"
    
    def convert_meters_to_km(self, _meters):
        if _meters > 0:
            return _meters*1000
        else:
            return -1

    def convert_squareMeters_to_squareFeet(self, _squareMeters):
        if _squareMeters >0:
            return _squareMeters*10.764
        else:
            return -1

    def convert_bits_to_bytes(self, bits):
        bytes_count = 0
        tmp_bits = bits
        while tmp_bits >=8:
            bytes_count+=1
            tmp_bits-=8

        return str(bytes_count) + ("byte" if bytes_count==1 else " bytes") +" and "+str(tmp_bits)+ (" bit" if tmp_bits==1 else " bits.")

    def add_converter(self, _converterTuple):
        if len(_converterTuple)==2:
            key = _converterTuple[0]
            value = _converterTuple[1]
            self.parserDict[key] = value

    def return_converters(self):
        converters = []
        for key in self.parserDict.keys():
            converters.append(key)
        return converters

    def convert_by_formula(self, formula, _values):
        values = _values
        ret_value = eval(formula)
        return ret_value

    def multi_convert(self, a, form):
        formula = self.parserDict[form]
        x = a
       
        return eval(formula)
    

class SimpleGeoFigCalc:
    def __init__(self, _geoFigFormulas):
        self.geoFigFormulas = _geoFigFormulas

    def return_formulas(self):
        formulas = []
        for key in self.geoFigFormulas.keys():
            formulas.append(key)
        return formulas 

    def add_new_formula(self, _newFormulaTuple):
        self.geoFigFormulas.update(_newFormulaTuple)

    def solve(self, _values, _formula):
        current_formula = self.geoFigFormulas[_formula]
        return current_formula

if __name__ == "__main__":
    
    dict = {
        "celcius->farenheit": "(x*1.8)+32",
        "square": "(x*x)",
        "farenheit->celcius":" (x-32)/1.8"
    }

    formulas = {
        "triangle":"a*h/2"
    }
    
    c = UniversalConverter(dict)
    s = SimpleGeoFigCalc(formulas)
    
    print(s.return_formulas())
    print(s.solve(1,"triangle"))