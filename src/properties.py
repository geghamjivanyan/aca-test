class Rational:

    def __init__(self, n, d):
        x = Rational.gcd(n, d)
        self.__nominator = n // x
        self.__denominator = d // x

    def __repr__(self):
        return "{}/{}".format(self.__nominator, self.__denominator)

    @classmethod
    def create_obj(cls, s):
        a = s.split('/')
        return cls(int(a[0]), int(a[1]))

    @staticmethod
    def gcd(x, y):
        c = 1
        for i in range(2, min(x, y)):
            if x % i == 0 and y % i == 0:
                c = i
        return c

    @property
    def nominator(self):
        print("GET")
        return self.__nominator

    @nominator.setter
    def nominator(self, x):
        print("SET")
        if x > 0:
            y = Rational.gcd(x, self.__denominator)
            self.__nominator = x // y
            self.__denominator = self.__denominator // y

r = Rational(4, 6)
r1 = Rational.create_obj("5/6")
print(r1.nominator)
r1.nominator = 15
print(r1)

