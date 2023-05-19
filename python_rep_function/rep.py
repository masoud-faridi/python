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
      
      
      
# https://stackoverflow.com/questions/71351333/repeat-function-in-python-similar-to-r/76288622#76288622
import string
letters =string.ascii_lowercase
letters =list(letters)



#> rep(letters[1:3],times=c(1,2,4))
#[1] "a" "b" "b" "c" "c" "c" "c"
rep(letters[0:3], each=[1,2,3] ,times=1  , length_out= -1)


#> rep(letters[1:3],each=2,len=15)
# [1] "a" "a" "b" "b" "c" "c" "a" "a" "b" "b" "c" "c" "a" "a" "b"
rep(letters[0:3], each=[2] ,times=1  , length_out= 15)


#> rep(letters[1:3],each=3,times=2)
# [1] "a" "a" "a" "b" "b" "b" "c" "c" "c" "a" "a" "a" "b" "b" "b" "c" "c" "c"
rep(letters[0:3], each=[3] ,times=2  )


#> rep(letters[c(TRUE,FALSE)],each=2)
# [1] "a" "a" "c" "c" "e" "e" "g" "g" "i" "i" "k" "k" "m" "m" "o" "o" "q" "q" "s" "s" "u" "u"
#[23] "w" "w" "y" "y"

rep(letters[::2], each=[2])


#rep(letters[c(TRUE,FALSE,TRUE,FALSE,FALSE)],each=2)
# [1] "a" "a" "c" "c" "f" "f" "h" "h" "k" "k" "m" "m" "p" "p" "r" "r" "u" "u" "w" "w" "z" "z"
#Example 6
TF=[True,False,True,False,False]
TF_all=rep(TF,length_out=len(letters))
index_letters=[letters[i] for i, x in enumerate(TF_all) if x]
rep(index_letters, each=[2])

#> rep(letters[c(TRUE,FALSE,TRUE,FALSE,FALSE)],each=2,len=25)
#[1] "a" "a" "c" "c" "f" "f" "h" "h" "k" "k" "m" "m" "p" "p" "r" "r" "u" "u" "w" "w" "z" "z"
#[23] "a" "a" "c"
TF=[True,False,True,False,False]
TF_all=rep(index,length_out=len(letters))
index_letters=[letters[i] for i, x in enumerate(TF_all) if x]
rep(index_letters, each=[2], length_out= 25)


#R code
#> rep(letters[1:3],each=3,times=2)
# [1] "a" "a" "a" "b" "b" "b" "c" "c" "c" "a" "a" "a" "b" "b" "b" "c" "c" "c"
# Python code
rep(letters[0:3], each=[3] ,times=2)
