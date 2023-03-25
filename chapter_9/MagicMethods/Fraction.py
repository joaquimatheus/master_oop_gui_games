import math

class Fraction():
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError('Numerator', numerator, 'must be an integer')
        if not isinstance(denominator, int):
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
        oOtherFractionEquivalentNumerator = oOtherFraction.numerator * otherMultiplicationFactor

        newNumerator = equivalentNumerator + oOtherFractionEquivalentNumerator

        oAddedFraction = Fraction(newNumerator, newDenominator)
        return oAddedFraction

    def __eq__(self, oOtherFraction):
        if not isinstance(oOtherFraction, Fraction):
            return False
        if (self.numerator == oOtherFraction.numerator) and (self.denominator == oOtherFraction.numerator):
            return True
        else:
            return False

oFraction1 = Fraction(1, 3)            
oFraction2 = Fraction(2, 5)
print('Fraction1\n', oFraction1)
print('Fraction2\n', oFraction2)

oSumFraction = oFraction1 + oFraction2
print('Sum is\n', oSumFraction)

print('Are fractions 1 and 2 equal2', (oFraction1 == oFraction2))
print()

oFraction3 = Fraction(-20, 80)
oFraction4 = Fraction(4, -16)
print('Fraction\n', oFraction3)
print('Fraction4\n', oFraction4)
print('Are fractions 3 and 4 equal?', (oFraction3 == oFraction4))
print()

oFraction5 = Fraction(5, 2)
oFraction6 = Fraction(500, 200)
print('Sum of 5/2 and 500/200\n', oFraction5 + oFraction6)
