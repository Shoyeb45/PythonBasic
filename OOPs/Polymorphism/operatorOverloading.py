class Complex:
    
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"

        return f"{self.real} - {-self.imaginary}i"
    def __add__(self, z2):
        re = self.real + z2.real
        im = self.imaginary + z2.imaginary
        return Complex(re, im)
    
    def __mul__(self, z):
        re = self.real * z.real - self.imaginary * z.imaginary
        im = self.imaginary * z.real + self.real * z.imaginary
        return Complex(re, im)
    
Z1 = Complex(1, 3)
Z2 = Complex(3, -2)


Z3 = Z1 + Z2
print(Z3.real, Z3.imaginary)
Z4 = Z1 * Z2
print(Z4.real, Z4.imaginary)
print(Z4)
