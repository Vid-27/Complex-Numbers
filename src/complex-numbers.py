# simple way using def
def complex_numbers(a, b):
    s = a + b * 1j
    return s


#complex numbers using class

def number(x, y):
    z = complex(x, y)
    print(-z)


class Complex_Number:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex_Number(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex_Number(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex_Number((self.real * other.real) - (self.imag * other.imag),
                              (self.imag * other.real) + (self.real * other.imag))

    def __neg__(self):
        return Complex_Number(-self.real, -self.imag)

    def conjugate(self):
        return Complex_Number(self.real, -self.imag)


