import sympy

if __name__=='__main__':
    x = sympy.Symbol("x")
    print (sympy.diff(sympy.sin(x**2)*x))