class Polynomial:
    def __init__(self, degree, coefs):
        self.degree = degree
        self.coefs = coefs

    def is_zero(self):
        if self.degree == 0 and self.coef == [0]:
            return True
        else:
            return False

    def coef(self, expon):
        if expon <= self.degree:
            return self.coefs[self.degree - expon]
        else:
            return 0

    def lead_exp(self):
        return self.degree

    def attach(self, coef, expon):
        if self.coef(expon):
            print("The term already exists.")
            raise SystemExit
        else:
            if expon > self.lead_exp():
                # The term's exponent to attach is bigger than the leading exponent
                # Change both the poly's degree and coefs
                new_coefs = [0 for i in range(expon + 1)]
                new_coefs[0] = coef
                new_coefs[-(self.degree + 1):] = self.coefs

                self.degree = expon
                self.coefs = new_coefs
            else:
                # The term's exponent to attach is not bigger than the leading exponent
                # Change only the poly's coefs
                self.coefs[self.degree - expon] = coef

    def remove(self, expon):
        if not self.coef(expon):
            print("The term doesn't exist.")
            raise SystemExit
        elif expon == self.lead_exp():
            # The term to remove is the leading term
            # Change both the poly's degree and coefs
            while True:
                self.degree -= 1
                self.coefs = self.coefs[1:]

                if self.coefs[0] or self.degree == 0:
                    break
        else:
            # The term to remove is not the leading term
            # Change only the poly's coefs
            self.coefs[self.degree - expon] = 0

    @staticmethod
    def zero():
        zero = Polynomial(0, [0])
        return zero

    @staticmethod
    def add(poly1, poly2):
        # Copy the parameter polys
        poly1 = Polynomial(poly1.degree, poly1.coefs)
        poly2 = Polynomial(poly2.degree, poly2.coefs)

        result = Polynomial.zero()
        while (not poly1.is_zero())

        return result


poly1 = Polynomial(4, [2, 0, 1, 0, 3])
poly2 = Polynomial(3, [1, 5, 1, 0])

result = Polynomial.add(poly1, poly2)
print(result.degree)
print(result.coefs)
print("\nOriginal poly1")
print(poly1.degree)
print(poly1.coefs)
