import numpy as np
def rep(lst, each=[1] ,times=1  , length_out= -1):
    if len(each) < len(lst):
        mul_each = len(lst) // len(each) + 1
        each = each * mul_each
        each=each[:len(lst)]
    ls=np.repeat(lst,repeats=each)
    ls=ls.tolist() * times
    if length_out != -1:
        if length_out < len(ls):
            ls[:length_out]
        else:
            mul = length_out // len(ls) + 1
            ls = ls * mul
        return ls[:length_out]
    return ls


import numpy as np
class list_rep(list):
    def __init__(self, *args):
        super().__init__(*args)
    def __rep__(self, each=[1] ,times=1  , length_out= -1):
        lst=list(self)
        if len(each) < len(lst):
            mul_each = len(lst) // len(each) + 1
            each = each * mul_each
            each=each[:len(lst)]
        ls=np.repeat(lst,repeats=each)
        ls=ls.tolist() * times
        if length_out != -1:
            if length_out < len(ls):
                ls[:length_out]
            else:
                mul = length_out // len(ls) + 1
                ls = ls * mul
            ls =ls[:length_out]
        return ls
