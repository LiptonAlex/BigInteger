class BigInteger:
    def __init__(self, value=0):
        self.value = value

    def setHex(self, hex_str):
        #встановлення значення з шістнадцяткового рядка
        self.value = int(hex_str, 16)

    def getHex(self):
        #отримання шістнадцяткового рядка
        return hex(self.value)

    #ПОБІТОВІ ОПЕРАЦІЇ

    def __and__(self, other):
        #операція І
        return BigInteger(self.value & other.value)

    def __xor__(self, other):
        #операція XOR
        return BigInteger(self.value ^ other.value)

    def __or__(self, other):
        #операція OR
        return BigInteger(self.value | other.value)

    def __lshift__(self, n):
        #побітовий зсув вліво
        return BigInteger(self.value << n)

    def __rshift__(self, n):
        #побітовий зсув вправо
        return BigInteger(self.value >> n)

    #АРИФМЕТИЧНІ ОПЕРАЦІЇ

    def __add__(self, other):
        #додавання
        return BigInteger(self.value + other.value)

    def __sub__(self, other):
        #віднімання
        return BigInteger(self.value - other.value)

    def __mul__(self, other):
        #множення
        return BigInteger(self.value * other.value)

    def __divmod__(self, other):
        #ділення та остача від ділення
        quotient, reminder = divmod(self.value, other.value)
        return (BigInteger(quotient), BigInteger(reminder))


big_int1 = BigInteger()
big_int2 = BigInteger()
big_int1.setHex("1a2b3c4d")
big_int2.setHex("abcdef")

result_and = big_int1 & big_int2  # Побітове І (AND)
result_or = big_int1 | big_int2    # Побітове АБО (OR)
result_xor = big_int1 ^ big_int2  # Побітове виключаюче АБО (XOR)
result_lshift = big_int1 << 2      # Побітовий зсув вліво на 2 біти
result_rshift = big_int1 >> 2      # Побітовий зсув вправо на 2 біти
result_add = big_int1 + big_int2  # Додавання
result_sub = big_int1 - big_int2  # Віднімання
result_mul = big_int1 * big_int2  # Множення
result_divmod = str(divmod(big_int1, big_int2))  # Ділення та залишок

print("I (AND): " + result_and.getHex())  # Виводить шістнадцятковий рядок
print("OR: " + result_or.getHex())   # Виводить шістнадцятковий рядок
print("XOR: " + result_xor.getHex())  # Виводить шістнадцятковий рядок
print("Зсув вліво: " + result_lshift.getHex())  # Виводить шістнадцятковий рядок
print("Зсув вправо:" + result_rshift.getHex())  # Виводить шістнадцятковий рядок
print("Додавання: " + result_add.getHex())  # Виводить шістнадцятковий рядок
print("Віднімання: " + result_sub.getHex())  # Виводить шістнадцятковий рядок
print("Множення: " + result_mul.getHex())  # Виводить шістнадцятковий рядок
print("Ділення та остача: " + result_divmod)        # Виводить ділення та залишок у формі кортежу