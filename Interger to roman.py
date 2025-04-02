class IntegerToRoman:
    def __init__(self):
        # Define the mappings of Roman numerals
        self.num_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def convert_to_roman(self, num):
        if num <= 0 or num > 3999:
            return "Invalid Input! Enter a number between 1 and 3999."
        
        roman_numeral = ""
        for value, symbol in self.num_to_roman:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral


# Example usage
converter = IntegerToRoman()
number = 1987
print(f"{number} in Roman numerals is {converter.convert_to_roman(number)}")
