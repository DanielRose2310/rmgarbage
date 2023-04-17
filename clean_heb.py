import re
import numpy as np
import string
alpha = list('אבגדהוזחטיכלמנסעפצקרשתךםןףץ')

finals = list('ךםןףץ')


def rle(message):
    encoded_string = np.array([])
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
            if (message[j] == message[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        encoded_string = np.append(encoded_string,count)
        i = j + 1
    return encoded_string


def rmg_toolong(x,length = 12):
    if len(x)>=length:
        return True
    else:
        return False

def rmg_bad_alnum_ratio(x,threshold = 0.5):
    str_len = len(x)

    nchar_alphanum = len(re.findall("[\u0590-\u05FF-Z0-9]", x))

    if (nchar_alphanum / str_len) <=threshold:
        return True
    else:
        return False

def rmg_consecutive_four_identical(x, n = 4):


    inds = rle(x)
    
    if any(inds > n):
        return True
    else:
        return False

def rmg_consecutive_three_identical(x, n = 3):


    inds = rle(x)
    
    if any(inds > n):
        return True
    else:
        return False

def rmg_has_two_distinct_puncts_inside(x):

    out1 = x[1:-1]
    
    out2 = len(out1) - len(out1.translate(str.maketrans('', '', string.punctuation)))

    if (out2 >= 2):
        return True
    else:
        return False


def rmg_three_finals(x):
    num_finals = 0
    for c in list(x):
        if c in finals:
            num_finals = num_finals+1
    if num_finals > 2:
        return True


def split_finals(x):
    num_finals = 0
    
    for position,c in enumerate(list(x)):
        if c in finals and position<len(x)-1:
            x = x[:position+1] + ' ' + x[position+1:]
            break
    return x
    

def clean(x):
    if any([
        rmg_three_finals(x),
      rmg_bad_alnum_ratio(x),
      rmg_consecutive_three_identical(x),
      #rmg_bad_consonant_vowel_ratio(x),
      #rmg_consecutive_four_identical(x),
      rmg_has_two_distinct_puncts_inside(x),
      #rmg_has_uppercase_within_lowercase(x),
      rmg_toolong(x),
      #rmg_uppercase_lowercase_ratio(x)
    ]):
        return ''
    else:
        return split_finals(x)


