class Fraction :
    def __init__(self,num, den,):
        assert den > 0
        self.num = num
        self.den = den
    def __str__(self):
        if self.den == 1 :
            
            return str(self.num)
        else :
            return (str(self.num) + "/" + str(self.den))
    def __egalite__(self,other) :
        if self.num*other.den == self.den * other.num :
            return True
        else :
            return False
   
F1,F2,F3,F4 = Fraction(3, 4) , Fraction(-8,1) , Fraction(2,3), Fraction(21,28)
print(F1)
print(F2)
print(F3)
print(F4)

print(F1.__egalite__(F4))
print(F2.__egalite__(F1))
print(F4.__egalite__(F4))
print(F4.__egalite__(F2))



