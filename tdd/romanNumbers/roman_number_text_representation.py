
class RomanNumberTextRepresentation(object):

    @staticmethod
    def _convertDigit(aDigit,
                      stringBuilder,
                      asOne='I',
                      asFive='V',
                      asTen='X'):
        if 1 <= aDigit <= 3:
            for _ in range(aDigit):
                stringBuilder += asOne
        elif aDigit == 4:
            stringBuilder += asOne + asFive
        elif 5 <= aDigit <= 8:
            stringBuilder += asFive
            for _ in range(5, aDigit):
                stringBuilder += asOne
        elif aDigit == 9:
            stringBuilder += asOne + asTen

        return stringBuilder

    @staticmethod
    def of(aNumber):
        stringBuilder = ""
        units = aNumber % 10
        tens = int((aNumber % 100) / 10)
        hundreds = int(aNumber / 100)

        stringBuilder = RomanNumberTextRepresentation._convertDigit(
            hundreds, stringBuilder, 'C', 'D', 'M')
        stringBuilder = RomanNumberTextRepresentation._convertDigit(
            tens, stringBuilder, 'X', 'L', 'C')
        stringBuilder = RomanNumberTextRepresentation._convertDigit(
            units, stringBuilder)

        return stringBuilder
