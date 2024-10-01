import math
class Convertion:
    def __init__(self, digit, number) -> None:
        self.digit = digit
        self.number = number
        
    def calculation(self):
        try:
            if self.digit < 2:
                raise ValueError
        except ValueError:
            print("digit must be integer greater than 2")
            return
        if self.digit > self.number:
            return self.number
        temp = int(math.log(self.number, self.digit))
        output = ''
        while temp >= 0:
            divisor = str(int(self.number / (self.digit ** temp)))
            output += divisor
            self.number = self.number % (self.digit ** temp)
            temp -= 1
        return output