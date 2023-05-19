# R index
# > letters[c(TRUE,FALSE)]
# [1] "a" "c" "e" "g" "i" "k" "m" "o" "q" "s" "u" "w" "y"

#> letters[c(TRUE,TRUE,FALSE)]
# [1] "a" "b" "d" "e" "g" "h" "j" "k" "m" "n" "p" "q" "s" "t" "v" "w" "y" "z"

#> letters[c(TRUE,TRUE,FALSE,FALSE,TRUE)]
# [1] "a" "b" "e" "f" "g" "j" "k" "l" "o" "p" "q" "t" "u" "v" "y" "z"


import itertools
import string
letters =string.ascii_lowercase
letters =list(letters)

zp=zip(letters,itertools.cycle([True,True,False,False,True]))
list(zp)
letters_2=[i for i,j in zip(letters,itertools.cycle([True,True,False,False,True])) if j]
letters_2


zp_longest=itertools.zip_longest(letters,[True,True,False,False,True])
list(zp_longest)
letters_3=[i for i,j in itertools.zip_longest(letters,[True,True,False,False,True]) if j]
letters_3
