import string
import copy
import math

class AdvNumber:
    def add_to_fraction(self, val, num_or_dom):
        num_or_dom[0] *= val

    def __init__(self, val1, val2=1, op="uxux"):
        self.num_numerator = [1]
        self.num_denominator = [1]
        self.var_numerator = []
        self.var_denominator = []
        
        if op == "uxux":
            self.num_numerator = [val1]
            self.num_denominator = [val2]
        else:
            if type(val1) == int:
                val1 = AdvNumber(val1)
            if type(val2) == int:
                val2 = AdvNumber(val2)
            self.combine(val1, val2, op)

    def get_reciprocal(self, val):
        temp = [copy.copy(val.num_numerator) , copy.copy(val.var_numerator)]
        val.num_numerator = val.num_denominator
        val.var_numerator = val.var_denominator
        val.num_denominator = temp[0]
        val.var_denominator = temp[1]
        return val
    # def __init__(self, num, variable_arr, op_for_each):
    #     self.val = str(num) + [i for i in variable_arr]

    # def __init__(self, exp1 : AdvNumber, exp2 : AdvNumber, op):
    #     self.val = str(exp1) + op + str(exp2)

    def combine(self, val1 , val2 , op : string):
        if val1.var_numerator == [] and val1.var_denominator == [] and val2.var_denominator == [] and val2.var_numerator == []:
            if op == "*":
                self.add_to_fraction(val1.num_numerator[0] , self.num_numerator)
                self.add_to_fraction(val2.num_numerator[0] , self.num_numerator)
                self.add_to_fraction(val1.num_denominator[0] , self.num_denominator)
                self.add_to_fraction(val2.num_denominator[0] , self.num_denominator)               
            elif op == "/":
                var2_inverse = self.get_reciprocal(val2)
                self.combine(val1, var2_inverse, "*")
            elif op == "+":
                lcm = math.lcm(val1.num_denominator[0], val2.num_denominator[0])
                self.add_to_fraction(lcm, self.num_denominator)
                val1_factor = lcm//val1.num_denominator[0]
                val2_factor = lcm//val2.num_denominator[0]
                val1.num_numerator[0] *= val1_factor
                val2.num_numerator[0] *= val2_factor
                self.add_to_fraction(val1.num_numerator[0] + val2.num_numerator[0], self.num_numerator)
            elif op == "-":
                val2.num_numerator[0] *= -1
                self.combine(val1, val2, '+')

        #
        # if type(val1) is int and type(val2) is int:
        #     if op == "/":
        #         self.add_to_fraction(val1, self.num_numerator)
        #         self.add_to_fraction(val2, self.num_denominator)
        #     else:
        #         result = basicArithmetic(val1, val2, op)
        #         self.add_to_fraction(result, self.num_numerator)
        # elif (type(val1) is str and type(val2) is int) or (type(val1) is int and type(val2) is str) :
        #     pass
        # elif type(val1) is str and type(val2) is str:
        #     pass


    def __str__(self):
        return(str(self.num_numerator) + " / " + str(self.num_denominator))