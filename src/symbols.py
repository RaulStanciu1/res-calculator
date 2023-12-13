from enum import Enum
from fractions import Fraction

class Variable:
    LIMIT_DENOMINATOR = 100000
    def __init__(self, conversion:str):
        """
            Constructor converts a conversion string to a variable object.
            Conversion strings has the following form:
            <NAME> <HEX_MIN> <HEX_MAX> <PHYS_MIN> <PHYS_MAX> <RES>
        """
        conversion_arr = conversion.split(" ")
        self.name = conversion_arr[0]
        self.hex_min = int(conversion_arr[1])
        self.hex_max = int(conversion_arr[2])
        self.phys_min = float(conversion_arr[3])
        self.phys_max = float(conversion_arr[4])
        self.res = Fraction(float(conversion_arr[5])).limit_denominator(Variable.LIMIT_DENOMINATOR)
    
        

class Operator(Enum):
    ADD="+"
    SUB="-"
    MUL="*"
    DIV="/"
    EQ="="
    ERR=""

def str_to_opp(opp_str:str)->Operator:
    if opp_str == "+":
        return Operator.ADD
    if opp_str == "-":
        return Operator.SUB
    if opp_str == "*":
        return Operator.MUL
    if opp_str == "/":
        return Operator.DIV
    if opp_str == "=":
        return Operator.EQ
    return Operator.ERR
    
    
class Paren(Enum):
    L_PAREN = "("
    R_PAREN = ")"
    ERR=""
    
def str_to_paren(paren_str:str)->Paren:
    if paren_str == "(":
        return Paren.L_PAREN
    if paren_str ==")":
        return Paren.R_PAREN
    return Paren.ERR