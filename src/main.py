from equation import Equation
from equation import Operator
from equation import Paren
from symbols import Variable
from solver import solve_equation

from sympy import simplify, sympify

def main():
    new_equation = Equation()
    new_equation.add_variable(Variable("X 0 255 0 127.5 0.5"))
    new_equation.add_symbol(Operator.EQ)
    new_equation.add_variable(Variable("Y -32768 32767 -3276.8 3276.7 0.1"))
    new_equation.add_symbol(Operator.MUL)
    new_equation.add_symbol(Paren.L_PAREN)
    new_equation.add_variable(Variable("Z -32768 32767 -40000 39998.77946071 1.22070313"))
    new_equation.add_symbol(Operator.ADD)
    new_equation.add_constant(2.5)
    new_equation.add_symbol(Paren.R_PAREN)
    new_equation.finish_eq()
    
    print("Simplified Equation: "+ solve_equation(new_equation))

if __name__ == "__main__":
    main()

