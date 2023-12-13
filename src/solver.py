from equation import Equation
from equation import Operator
from equation import Paren
from symbols import Variable

from sympy import simplify, sympify


def solve_equation(eq:Equation):
    if not eq.is_valid():
        raise Exception("Invalid Equation")
    new_eq_str = eq.as_str().split("=")
    
    expr = sympify(new_eq_str)[1]
    simplified_expr = simplify(expr)
    return (new_eq_str[0] +"= " + str(simplified_expr))