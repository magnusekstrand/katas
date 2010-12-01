# Module FizzBuzz

class FizzBuzz():
    
    def __init__(self):
        pass

    def is_fizz(self, x):
        if (x % 3 == 0 or str(x).find('3') > -1):
            return True
        return False

    def is_buzz(self, y):
        if (y % 5 == 0 or str(y).find('5') > -1):
            return True
        return False

    def filter(self, integers):
        resultlist = []
        for i in integers:
            resultlist.append(self.convert(i))
        return resultlist

    def convert(self, integer):
        converted = ""
        if self.is_fizz(integer): converted += "Fizz"
        if self.is_buzz(integer): converted += "Buzz"
        if converted == "": converted = integer
        return converted


