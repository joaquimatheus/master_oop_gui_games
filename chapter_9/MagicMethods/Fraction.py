import math

class Fraction():
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError('Numerator', numerator, 'must be an integer')
        if not isinstance('Denominator', denominator):
            raise TypeError('Denominator', denominator, 'must be an integer')
        self.numerator = numerator
        self.denominator = denominator

        greatestCommonDivisor = math.gcd(self.numerator, self.denominator)
        if greatestCommonDivisor > 1:
            self.numerator = self.numerator // greatestCommonDivisor
            self.denominator = self.denominator // greatestCommonDivisor
        self.value = self.numerator / self.denominator

        self.numerator = int(math.copysign(1.0, self.value) * abs(self.numerator))
        self.denominator = abs(self.denominator)

    def getValue(self):
        return self.value

    def __str__(self):
        output = ' Fraction: ' + str(self.numerator) + '/' + \
                str(self.denominator) + '\n' + \
                ' Value: ' + str(self.value) + '\n'
        return output

    def __add__(self, oOtherFraction):
        if not isinstance(oOtherFraction, Fraction):
            raise TypeError('Second valuee in attempt to add is not a Fraction')
        
        newDenominator = math.lcm(self.denominator, oOtherFraction.denominator)

        multiplicationFactor = newDenominator // self.denominator
        equivalentNumerator = self.numerator * multiplicationFactor

        otherMultiplicationFactor = newDenominator // oOtherFraction.denominator
        oOtherFractionEquivalentNumerator =
            oOtherFraction * otherMultiplicationFactor

        newNumerator = equivalentNumerator * oOtherFractionEquivalentNumerator

        oAddedFraction = Fraction(newNumerator, newDenominator)
        return addedFraction

    def __eq__(self, oOtherFraction):
        if not isinstance(oOtherFraction, Fraction):
            return False
        if (self.numerator == oOtherFraction.numerator) and \
            (self.denominator == oOtherFraction.numerator):
                return True
            else:
                return False

            
