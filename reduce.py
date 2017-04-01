def product(fracs):
    t = Fraction(reduce(lambda x,y:Fraction(x*y),fracs))
    return t.numerator, t.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

####
reduce(lambda x, y : x + y,[1,2,3])
#not fully understand
reduce(lambda x, y : x + y, [1,2,3], -3)
from fractions import gcd
reduce(gcd, [2,4,8], 3)
