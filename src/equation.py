from enum import Enum
from fractions import Fraction
from symbols import Variable
from symbols import Operator
from symbols import Paren
    
class Equation:
    def __init__(self):
        self.eq = [] #Equation List
        self.paren_ctr = 0 #Counter For Parenthesis
        self.eq_ctr = 0 #Counter for Equal Symbols
        self.var_ctr = 0 #Counter for Variable Symbols
        self.is_finished = False
        
    def __str__(self):
        equation_str = ""
        for token in self.eq:
            if isinstance(token, Operator) or isinstance(token, Paren):
                equation_str += str(token.value)
            else:
                equation_str += str(token)
            equation_str += " "
        return equation_str
        
    def add_symbol(self,symbol:(Operator | Paren)):
        """Function that adds a symbol to the current Equation
        Args:
            opp (Operator | Paren): The Symbol To be Added
        """
        self.eq.append(symbol)
        if isinstance(symbol, Operator) and symbol == Operator.EQ:
            self.eq_ctr += 1
        elif isinstance(symbol, Paren):
            if symbol == Paren.L_PAREN:
                self.paren_ctr += 1
            elif symbol == Paren.R_PAREN:
                self.paren_ctr -= 1
        
    def __add_int(self, num:int):
        self.eq.append(num)    
    
    def __add_float(self, num:float):
        if num == int(num):
            self.__add_int(int(num))
        self.__add_fraction(Fraction(num).limit_denominator(Variable.LIMIT_DENOMINATOR))
    
    def __add_fraction(self, frac:Fraction):
        if frac.numerator != 1:
            self.__add_int(frac.numerator)
        self.add_symbol(Operator.DIV)
        self.__add_int(frac.denominator)
        
    
    def add_constant(self, constant:(float|int|Fraction)):
        """Function that adds a constant to the current Equation
            The constant can be a number(float or int) or a Fraction
        Args:
            constant (float | int | Fraction): the constant to be added to the Equation
        """
        if isinstance(constant, int):
            self.__add_int(constant)
        elif isinstance(constant, float):
            self.__add_float(constant)
        elif isinstance(constant, Fraction):
            self.__add_fraction(constant)
        
    def add_variable(self, var:Variable):
        """Function that adds a variable to the current Equation

        Args:
            var (Variable): The Variable to be added
        """
        self.eq.append(var.name)
        resolution_frac = var.res
        if isinstance(resolution_frac, float) and resolution_frac == 1.0:
            pass
        elif resolution_frac.numerator == 1:
            if resolution_frac.denominator == 1:
                pass
            else:
                self.eq.append(Operator.DIV)
                self.eq.append(var.res.denominator)
        else:
            self.add_symbol(Operator.MUL)
            self.add_constant(var.res)
        self.var_ctr += 1
            
    def is_valid(self):
        """Function that validates the current Equation object

        Returns:
            _type_: True if the equation is valid, False otherwise
        """
        if self.eq_ctr != 1:
            return False
        if self.paren_ctr !=0 :
            return False
        if not self.is_finished:
            return False
        if isinstance(self.eq[len(self.eq)-1], Operator):
            return False
        for symbol in self.eq:
            if symbol == Operator.ERR or symbol == Paren.ERR:
                return False
        
        return True

    def as_str(self) -> str:
        equation_str = ""
        for token in self.eq:
            if isinstance(token, Operator) or isinstance(token, Paren):
                equation_str += str(token.value)
            else:
                equation_str += str(token)
            equation_str += " "
        return equation_str
    
    def finish_eq(self):
        if self.eq[1] == Operator.EQ:
            return
        i = 1
        while self.eq[i] != Operator.EQ:
            if self.eq[i] == Operator.MUL:
                self.eq.append(Operator.DIV)
            elif self.eq[i] == Operator.DIV:
                self.eq.append(Operator.MUL)
            else:
                self.eq.append(self.eq[i])
            i +=1
        # Other than the Output and = remove the rest
        del self.eq[1:i]
        self.is_finished = True
                    
    
    
    
    